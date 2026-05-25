"""Parametrized recursion test that stresses the worker-thread stack while
linetrace coverage is enabled, to reproduce the Windows GHA exit-code-139
segfault seen in cuda-python's coverage step.

Run via ci/tools/run_pytest_with_stack.py so the recursion executes on a
thread whose stack size is controlled by --stack-mb.
"""

import sys
import pytest

from mypackage import deep_recursion, chained_calls


if deep_recursion is None or chained_calls is None:
    pytest.skip(
        "Cython recursion module not built (need COVERAGE_MODE=1 + pip install -e .)",
        allow_module_level=True,
    )

# Set high enough that Cython linetrace tracing per frame plus the
# coverage.py C tracer's per-line overhead can exhaust an 8 MB stack
# on Windows.  If 8 MB is sufficient, these all pass; if not, the
# process segfaults and faulthandler dumps a stack to stderr.
DEPTHS = [100, 500, 1000, 2000, 5000, 10000]


@pytest.mark.parametrize("depth", DEPTHS)
def test_deep_recursion(depth):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), depth + 200))
    result = deep_recursion(depth)
    assert result == depth


@pytest.mark.parametrize("depth", DEPTHS)
def test_chained_calls(depth):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), depth + 200))
    result = chained_calls(depth)
    assert result == depth * 3  # each frame adds 0+1+2 = 3
