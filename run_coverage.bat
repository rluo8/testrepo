@echo off
REM Build and test with coverage on Windows

echo ========================================
echo Build and test with coverage
echo ========================================
echo.

REM Set coverage mode
set COVERAGE_MODE=1

echo Step 1: Clean previous build
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del /q mypackage\*.c 2>nul
del /q mypackage\*.cpp 2>nul
del /q mypackage\*.pyd 2>nul

echo.
echo Step 2: Build with coverage support
pip install -e .

echo.
echo Step 3: Run tests with coverage
pytest -v --cov=.\mypackage --cov-context=test --cov-config=.coveragerc tests
coverage xml
coverage html
coverage report --show-missing

echo.
echo ========================================
echo Done!
echo Coverage report: htmlcov\index.html
echo ========================================

pause
