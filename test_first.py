def test_1():
    a=21
    b=21
    assert a==b

def test_2():
    title= 'selenium'
    text = 'Selenium webdriver installed.'
    assert title in text, "Title not found in text."