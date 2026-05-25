#!/usr/bin/env python3

"""Run pytest on a worker thread with a configurable stack size.

Mirrors cuda-python/ci/tools/run_pytest_with_stack.py so we can reproduce
the Windows GHA exit-code-139 segfault that occurs under Cython linetrace
coverage. Adds faulthandler diagnostics so the crash actually prints a
Python stack to stderr (the upstream version does not enable faulthandler,
which is why the NVIDIA CI log shows no traceback before the segfault).
"""

import argparse
import concurrent.futures
import faulthandler
import os
import sys
import threading

faulthandler.enable(file=sys.stderr, all_threads=True)

import pytest


def _worker(pytest_args):
    faulthandler.enable(file=sys.stderr, all_threads=True)
    print(f"[stackdiag] worker thread started, stack_size={threading.stack_size()} bytes", flush=True)
    return pytest.main(pytest_args)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stack-mb", type=int, default=8)
    parser.add_argument("--cwd", default=None)
    args, pytest_args = parser.parse_known_args()

    if args.cwd:
        os.chdir(args.cwd)

    print(f"[stackdiag] python={sys.executable}", flush=True)
    print(f"[stackdiag] version={sys.version}", flush=True)
    print(f"[stackdiag] cwd={os.getcwd()}", flush=True)
    print(f"[stackdiag] stack-mb={args.stack_mb}", flush=True)
    print(f"[stackdiag] pytest_args={pytest_args}", flush=True)

    threading.stack_size(args.stack_mb * 1024 * 1024)

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        code = pool.submit(_worker, pytest_args).result()

    sys.exit(code)


if __name__ == "__main__":
    main()
