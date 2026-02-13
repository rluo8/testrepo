# Setup script for building Cython extensions
import os
import sys
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# Check for coverage mode
COVERAGE_MODE = bool(int(os.environ.get("COVERAGE_MODE", "0")))

# DEBUG: Print what we got
print("=" * 60)
print(f"DEBUG: COVERAGE_MODE environment = '{os.environ.get('COVERAGE_MODE', 'NOT SET')}'")
print(f"DEBUG: COVERAGE_MODE evaluated as = {COVERAGE_MODE}")
print("=" * 60)
print()

# Cython build directory
build_dir = "." if COVERAGE_MODE else "build/cython"

# Compiler directives
compiler_directives = {
    "language_level": 3,
    "embedsignature": True,
    "binding": True,
}

if COVERAGE_MODE:
    print("=" * 60)
    print("Building with COVERAGE_MODE enabled")
    print(f"  - build_dir: {build_dir}")
    print(f"  - linetrace: True")
    print(f"  - compiler_directives: {compiler_directives}")
    print("=" * 60)
    print()
    compiler_directives["linetrace"] = True

# Extra compile args
extra_compile_args = []
if COVERAGE_MODE:
    extra_compile_args += ["-DCYTHON_TRACE_NOGIL=1"]

# Define extensions
extensions = [
    Extension(
        "mypackage.cython_math",
        sources=["mypackage/cython_math.pyx"],
        extra_compile_args=extra_compile_args,
    ),
]

# Cythonize
print(f"DEBUG: About to cythonize with directives: {compiler_directives}")
print(f"DEBUG: build_dir = {build_dir}")
print()

ext_modules = cythonize(
    extensions,
    compiler_directives=compiler_directives,
    build_dir=build_dir,
)

print(f"DEBUG: Cythonize completed")
print()

# Setup options
setup_options = {
    "name": "mypackage",
    "version": "0.1.0",
    "packages": find_packages(),
    "ext_modules": ext_modules,
    "install_requires": [
        "numpy",
    ],
    "python_requires": ">=3.8",
    "zip_safe": False,
}

# Package data for coverage mode
if COVERAGE_MODE:
    setup_options["package_data"] = {"mypackage": ["*.cpp", "*.c"]}  # Include both .c and .cpp
    setup_options["exclude_package_data"] = None
else:
    setup_options["exclude_package_data"] = {"mypackage": ["*.cpp", "*.c"]}

setup(**setup_options)
