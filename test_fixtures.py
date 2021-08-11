import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome(r'C:\Users\lenovo\eclipse-workspace\libs\chromedriver')
    driver.maximize_window()
    yield
    driver.quit()
    print("Close Browser")

def test_1(setup):
    driver.get("https://www.google.com/")
    print("Test1 executed")

def test_2(setup):
    driver.get("https://www.rediff.com/")
    print("Test2 executed")

def test_3(setup):
    driver.get("https://www.python.org/")
    print("Test3 executed")