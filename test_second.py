import pytest
import sys

@pytest.mark.smoke
def test_login():
    print("Login successful.")

@pytest.mark.regression
def test_loginverify():
    print("Login verify successful.")


@pytest.mark.skipif(sys.version_info>(3,8),reason="python version not supported on this machine.")
def test_loginverify():
    print("Login verify successful.")


@pytest.mark.smoke
def test_logout():
    print("Logout successful.")