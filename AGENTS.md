# AGENTS.md

Rules for AI coding agents working in this repository. When this project is checked out inside its parent research workspace, they are followed together with the workspace-level `AGENTS.md` (not included in this repository).

- Before starting, read `README.md` and the files you plan to change, and confirm the existing run flow.
- Keep the existing directory layout and make only the minimal change needed inside this project.
- `README.md` documents the actual layout and how to run the project; `AGENTS.md` holds the code-writing rules.
- Do not change random seeds, data splits, features, evaluation metrics, or experiment parameters without a request. Keep the baseline analysis separate from alternative experiments, and compare their results.
- Keep existing file names, code style, and dependencies, and do not refactor anything unrelated to the request.
- Preserve input data, models, and results, and save generated output to the existing output locations.
- After a change, run the related `tests/` and check the input/output contract.
- Do not report unverified inputs, external services, or experiments as complete.
