"""Calculate and export pitcher Snell Scores."""

from pathlib import Path

import pandas as pd

from snell_score import add_pitcher_scores, year_over_year_correlation

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "raw" / "pitcher.csv"
OUTPUT_PATH = ROOT / "outputs" / "tables" / "snellscorepitcher.csv"


def main() -> None:
    data = pd.read_csv(INPUT_PATH)
    scored = add_pitcher_scores(data).dropna(
        subset=["bb_percent_scale", "meatball_scale", "snell_score"]
    )
    qualified = scored[
        (scored["bb_percent_scale"] >= 60)
        & (scored["meatball_scale"] >= 60)
    ]
    columns = [
        "last_name, first_name",
        "year",
        "bb_percent",
        "bb_percent_scale",
        "meatball_percent",
        "meatball_scale",
        "snell_score",
    ]
    table = qualified[columns].sort_values("snell_score", ascending=False)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(OUTPUT_PATH, index=False)

    correlation = year_over_year_correlation(scored)
    print(f"Pitcher year-over-year Snell Score correlation: {correlation:.3f}")
    print(f"Saved {len(table):,} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

