import numpy as np
import pandas as pd
import pytest

from snell_score import (
    add_hitter_scores,
    add_pitcher_scores,
    standardized,
    year_over_year_correlation,
)


def test_standardized_uses_population_statistics() -> None:
    result = standardized(pd.Series([1.0, 2.0, 3.0]))
    assert result.mean() == pytest.approx(0.0)
    assert result.std(ddof=0) == pytest.approx(1.0)


def test_hitter_score_rewards_lower_rates() -> None:
    data = pd.DataFrame(
        {
            "last_name, first_name": ["A", "B", "C"],
            "year": [2024, 2024, 2024],
            "bb_percent": [5.0, 10.0, 15.0],
            "oz_swing_percent": [20.0, 30.0, 40.0],
        }
    )
    result = add_hitter_scores(data)
    assert result.loc[0, "snell_score"] > result.loc[2, "snell_score"]


def test_pitcher_score_rewards_walks_and_avoiding_meatballs() -> None:
    data = pd.DataFrame(
        {
            "last_name, first_name": ["A", "B", "C"],
            "year": [2024, 2024, 2024],
            "bb_percent": [15.0, 10.0, 5.0],
            "meatball_percent": [2.0, 5.0, 8.0],
        }
    )
    result = add_pitcher_scores(data)
    assert result.loc[0, "snell_score"] > result.loc[2, "snell_score"]


def test_year_over_year_uses_only_consecutive_seasons() -> None:
    data = pd.DataFrame(
        {
            "last_name, first_name": ["A", "A", "A", "B", "B"],
            "year": [2020, 2021, 2023, 2020, 2021],
            "snell_score": [10.0, 20.0, 999.0, 30.0, 40.0],
        }
    )
    result = year_over_year_correlation(data)
    assert result == pytest.approx(1.0)


def test_constant_series_returns_nan_scores() -> None:
    data = pd.DataFrame(
        {
            "last_name, first_name": ["A", "B"],
            "year": [2024, 2024],
            "bb_percent": [10.0, 10.0],
            "oz_swing_percent": [20.0, 20.0],
        }
    )
    result = add_hitter_scores(data)
    assert np.isnan(result["snell_score"]).all()

