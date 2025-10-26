#!/bin/bash
rm -rf .venv
rm -rf pyproject.toml
uv init
uv add qiskit matplotlib pylatexenc