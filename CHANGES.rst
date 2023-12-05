=========
Changelog
=========

Insert-license-header 1.0.0 (2023-11-07)
================================================
* Tool is a standalone pypi tool and no longer a pre-commit hook
    * Rename project to `insert-license-header`
* Remove hard-coded default LICENSE.header
* Introduce `--license-base64` flag that allows to pass a base64 encoded license instead of specifying a file path via `--license-filepath`


Pre-commit-insert-qc-license v1.7.1 (2023-11-07)
================================================
* Refactoring
    * Remove unnecessary pre-commit-hooks
    * Rename module folder `pre-commit-hooks` to `pre-commit-insert-qc-license`
    * `default_license.py` => `LICENSE.header`
* Port project to use exclusively `pyproject.toml`
* Add Python `3.12` to CI


Pre-commit-insert-qc-license v1.7.0 (2023-10-25)
================================================
* Introduce `--dynamic-years` flag
* Option to omit `--license-filepath`: default QC license is taken from `pre-commit-hooks/default_license.py`
* Add execution of `pytest` to CI workflow

