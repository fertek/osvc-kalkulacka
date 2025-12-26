# Repository Guidelines

## Project Structure & Module Organization

- `osvc_kalkulacka/` is the main package. `osvc_kalkulacka/core.py` holds calculation logic; `osvc_kalkulacka/cli.py` defines the Click CLI.
- `osvc_kalkulacka/data/` contains embedded TOML defaults (shipped in the wheel).
- `tests/` contains pytest suites such as `test_compute.py`.
- `osvc_kalkulacka.py` is a small convenience entrypoint that calls the CLI.

## Build, Test, and Development Commands

- `python -m pip install -e .` installs the package in editable mode for local development.
- `python osvc_kalkulacka.py --help` runs the CLI without installing the console script.
- `python -m pytest` runs the test suite.
- Packaging uses Hatchling via PEP 517. Use your preferred build frontend (for example, `python -m build`) if installed.

## Coding Style & Naming Conventions

- Use 4-space indentation and standard Python typing conventions (`str | None`, `dict[int, ...]`).
- Prefer explicit, descriptive names (`load_year_defaults`, `child_bonus_annual_tiers`).
- Modules and functions use `snake_case`; constants are `UPPER_SNAKE_CASE`.
- Data file names follow `year_*.toml` patterns in `osvc_kalkulacka/data/`.

## Testing Guidelines

- Tests are written with pytest and live in `tests/` using the `test_*.py` naming convention.
- Add or update tests when adjusting calculation logic in `osvc_kalkulacka/core.py`.
- Run `python -m pytest` before submitting changes.

## Commit & Pull Request Guidelines

- Git history shows short, direct messages (for example, "first commit"). Keep commit subjects concise and imperative.
- PRs should include a brief summary, the motivation for the change, and test results (paste the `pytest` command run).
- If CLI output changes, include a short before/after snippet in the PR description.

## Configuration & Data

- User overrides are read from `${USER_DIR}/year_presets.toml` and `${USER_DIR}/year_defaults.override.toml`.
- Environment variables `OSVC_PRESETS_PATH` and `OSVC_DEFAULTS_PATH` can override these locations.
