# tinystats

[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg?branch=dev)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/OWNER/REPO/branch/dev/graph/badge.svg)](https://codecov.io/gh/OWNER/REPO)

Small summary statistics for a list of numbers. A team builds this package to practice Git, pull requests, test-driven development (TDD), and continuous integration (CI).

Replace `OWNER/REPO` in the badges with the GitHub owner and repo name.

## Install for development

```bash
git clone git@github.com:OWNER/REPO.git
cd REPO
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run the checks

These are the same checks that CI runs on every pull request:

```bash
pytest --cov --cov-report=term-missing
ruff check .
ruff format --check .
```

## Use

```python
>>> from tinystats import mean
>>> mean([1, 2, 3])
2.0
```

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before you start.
