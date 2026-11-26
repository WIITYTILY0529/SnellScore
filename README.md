# SnellScore

A small research project that rates MLB hitters and pitchers on walk tendency and zone-related plate-discipline metrics. Each component is converted to the 20–80 scouting scale, and the components are summed into a single **Snell Score**.

The name nods to Blake Snell, a pitcher known for combining high walk rates with hard-to-hit pitches. He ranks near the top of the pitcher table.

## Metric definition

| Player type | Component 1 | Component 2 |
|---|---|---|
| Hitter | Walk rate (`bb_percent`), **lower** is better | Out-of-zone swing rate (`oz_swing_percent`), **lower** is better |
| Pitcher | Walk rate (`bb_percent`), **higher** is better | Meatball rate (`meatball_percent`), **lower** is better |

- Each component is standardized with population z-scores over all player-seasons in the input file, then mapped to the 20–80 scale (`50 + 10 × z`).
- `snell_score` is the sum of the two scaled components, so 100 is average.
- The pitcher table keeps only player-seasons where **both** scaled components are at least 60.
- Each script also reports the year-over-year correlation of Snell Score between consecutive seasons of the same player.

These definitions formalize the logic of the original exploratory code. The baseball interpretation of the metric and the filter thresholds have not been validated further.

## Repository layout

```text
data/raw/          Input CSVs (season-level plate-discipline metrics, 2015–2024)
src/snell_score/   Reusable scoring functions
scripts/           Analysis entry points
outputs/tables/    Generated score tables
tests/             Unit tests for the scoring logic
archive/           Original exploratory scripts, kept for reference
```

See [`data/README.md`](data/README.md) for the input data and [`archive/README.md`](archive/README.md) for the archived scripts.

## Installation

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"
```

A fully pinned Windows environment is also provided:

- `requirements-windows.txt` lists the direct dependencies, including notebook and archive-script extras.
- `requirements-windows.lock.txt` records the exact versions used for the published results.

```powershell
python -m pip install -r requirements-windows.lock.txt
```

## Usage

Run the scripts from the repository root:

```bash
python scripts/run_hitter_analysis.py
python scripts/run_pitcher_analysis.py
```

They write:

- `outputs/tables/snellscorehitter.csv`
- `outputs/tables/snellscorepitcher.csv`

The library functions can also be used directly:

```python
import pandas as pd
from snell_score import add_hitter_scores, year_over_year_correlation

scored = add_hitter_scores(pd.read_csv("data/raw/hitter.csv"))
print(year_over_year_correlation(scored))
```

## Tests

```bash
pytest
```
