# Data

`raw/` holds the original hitter and pitcher input files, kept unchanged.

| File | Contents | Rows | Seasons |
|---|---|---|---|
| `raw/hitter.csv` | Hitter season-level plate-discipline metrics (`bb_percent`, `z_swing_percent`, `oz_swing_percent`) | 1,375 | 2015–2024 |
| `raw/pitcher.csv` | Pitcher season-level metrics (`k_percent`, `bb_percent`, `meatball_percent`) | 1,106 | 2015–2024 |

Each row is one player-season, identified by `last_name, first_name`, `player_id`, and `year`. The column layout matches Baseball Savant (Statcast) custom leaderboard exports. Rates are percentages.

Raw files are never overwritten. Computed results are written to `../outputs/tables/`.
