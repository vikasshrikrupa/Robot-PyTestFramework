import pytest
import sys


@pytest.mark.parametrize("username,pw",
                         [
                             ('Selenium','Webdriver'),
                             ('Python','Import'),
                             ('C++', 'cpp'),
                         ]
                        )
def test_login(username,pw):
    print(username)
    print(pw)