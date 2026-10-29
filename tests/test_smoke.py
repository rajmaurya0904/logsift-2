"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import logsift_2


def test_version_is_set() -> None:
    assert logsift_2.__version__
