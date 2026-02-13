@echo off
REM Rebuild with coverage support for Cython

echo ========================================
echo Rebuild with Cython Coverage Support
echo ========================================
echo.

REM Step 1: Set environment variable
set COVERAGE_MODE=1
echo [1/5] Set COVERAGE_MODE=1

REM Step 2: Verify environment
python -c "import os; print('      COVERAGE_MODE =', os.environ.get('COVERAGE_MODE', 'NOT SET'))"
echo.

REM Step 3: Clean old build
echo [2/5] Cleaning old build...
pip uninstall -y mypackage
rmdir /s /q build 2>nul
rmdir /s /q mypackage.egg-info 2>nul
del /q mypackage\*.c 2>nul
del /q mypackage\*.cpp 2>nul
del /q mypackage\*.pyd 2>nul
del /q mypackage\*.so 2>nul
echo.

REM Step 4: Build with coverage
echo [3/5] Building with COVERAGE_MODE=1...
pip install -e .
echo.

REM Step 5: Run tests
echo [4/4] Running tests with coverage...
pytest -v --cov=.\mypackage --cov-context=test --cov-config=.coveragerc tests
coverage html
coverage report --show-missing
echo.

echo ========================================
echo Done! Check htmlcov\index.html
echo ========================================

pause
