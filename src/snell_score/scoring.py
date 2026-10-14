"""Core Snell Score calculations."""

from __future__ import annotations

import numpy as np
import pandas as pd

PLAYER_COLUMN = "last_name, first_name"


def standardized(series: pd.Series) -> pd.Series:
    """Return population z-scores for a numeric series."""
    numeric = pd.to_numeric(series, errors="coerce")
    standard_deviation = numeric.std(ddof=0)
    if pd.isna(standard_deviation) or np.isclose(standard_deviation, 0.0):
        return pd.Series(np.nan, index=series.index, dtype=float)
    return (numeric - numeric.mean()) / standard_deviation


def scale_20_80(z_scores: pd.Series) -> pd.Series:
    """Convert z-scores to a scouting-style scale centered at 50."""
    return 50 + (z_scores * 10)


def add_hitter_scores(data: pd.DataFrame) -> pd.DataFrame:
    """Add hitter Snell Score components without modifying the input."""
    required = {PLAYER_COLUMN, "year", "bb_percent", "oz_swing_percent"}
    _require_columns(data, required)

    result = data.copy()
    result["bb_percent_z"] = -standardized(result["bb_percent"])
    result["bb_percent_scale"] = scale_20_80(result["bb_percent_z"])
    result["oz_swing_z"] = -standardized(result["oz_swing_percent"])
    result["oz_swing_scale"] = scale_20_80(result["oz_swing_z"])
    result["snell_score"] = result["bb_percent_scale"] + result["oz_swing_scale"]
    return result


def add_pitcher_scores(data: pd.DataFrame) -> pd.DataFrame:
    """Add pitcher Snell Score components without modifying the input."""
    required = {PLAYER_COLUMN, "year", "bb_percent", "meatball_percent"}
    _require_columns(data, required)

    result = data.copy()
    result["bb_percent_z"] = standardized(result["bb_percent"])
    result["bb_percent_scale"] = scale_20_80(result["bb_percent_z"])
    result["meatball_z"] = -standardized(result["meatball_percent"])
    result["meatball_scale"] = scale_20_80(result["meatball_z"])
    result["snell_score"] = result["bb_percent_scale"] + result["meatball_scale"]
    return result


def year_over_year_correlation(data: pd.DataFrame) -> float:
    """Calculate correlation between consecutive observed player seasons."""
    required = {PLAYER_COLUMN, "year", "snell_score"}
    _require_columns(data, required)

    ordered = data.sort_values([PLAYER_COLUMN, "year"]).copy()
    ordered["next_year"] = ordered.groupby(PLAYER_COLUMN)["year"].shift(-1)
    ordered["next_year_snell"] = ordered.groupby(PLAYER_COLUMN)["snell_score"].shift(-1)
    consecutive = ordered[ordered["next_year"] == ordered["year"] + 1]
    return float(consecutive["snell_score"].corr(consecutive["next_year_snell"]))


def _require_columns(data: pd.DataFrame, required: set[str]) -> None:
    missing = required.difference(data.columns)
    if missing:
        names = ", ".join(sorted(missing))
        raise ValueError(f"Missing required columns: {names}")

