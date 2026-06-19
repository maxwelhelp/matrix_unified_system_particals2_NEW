#!/usr/bin/env python3
"""Run Weaver CLI with numba cache disabled for this local environment."""
import sys

import numba


_orig_njit = numba.njit


def _njit_no_cache(*args, **kwargs):
    kwargs.pop("cache", None)
    return _orig_njit(*args, **kwargs)


numba.njit = _njit_no_cache

from weaver.train import main  # noqa: E402


if __name__ == "__main__":
    sys.argv[0] = "weaver"
    main()
