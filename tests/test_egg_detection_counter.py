"""Package level tests"""

from egg_detection_counter import __version__


def test_version() -> None:
    """Unit test for checking the version of the code"""
    assert __version__ == "0.2.0"
