from Hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    assert hello("David") == "Hello, David"


