#!/bin/bash

echo "========================================"
echo "Build and test with coverage"
echo "========================================"
echo

# Set coverage mode
export COVERAGE_MODE=1

echo "Step 1: Clean previous build"
rm -rf build/ dist/ *.egg-info mypackage/*.c mypackage/*.cpp mypackage/*.so

echo
echo "Step 2: Build with coverage support"
pip install -e .

echo
echo "Step 3: Run tests with coverage"
pytest -v --cov=./mypackage --cov-context=test --cov-config=.coveragerc tests
coverage xml
coverage html
coverage report --show-missing

echo
echo "========================================"
echo "Done!"
echo "Coverage report: htmlcov/index.html"
echo "========================================"
