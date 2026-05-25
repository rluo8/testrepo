# Cython module used by the Windows stack-crash reproduction workflow.
#
# Built with linetrace=True under COVERAGE_MODE=1 so that every Python-level
# line in this module also calls __Pyx_TraceLine, which is the same code path
# that triggers the segfault in cuda.bindings during cuda-python's Windows
# coverage CI step.

def deep_recursion(int n):
    """Recurse n times. With linetrace enabled, each frame carries both
    Python interpreter stack overhead and Cython's tracing overhead, so this
    is a controlled way to stress the worker thread's stack."""
    if n <= 0:
        return 0
    return 1 + deep_recursion(n - 1)


def chained_calls(int n):
    """Mix recursion with intermediate work so a frame is not just a tail
    call. Reproduces the shape of real module-level imports more closely
    than a single-line recurse."""
    cdef int acc = 0
    cdef int i
    if n <= 0:
        return 0
    for i in range(3):
        acc += i
    acc += chained_calls(n - 1)
    return acc
