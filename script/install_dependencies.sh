#!/bin/bash

SCRIPT_DIR="$(cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P)"
PROJECT_DIR="${SCRIPT_DIR}/.."

pip install pre-commit

# Initialize pre-commit
pre-commit install
pre-commit install -t commit-msg
pre-commit install --install-hooks
