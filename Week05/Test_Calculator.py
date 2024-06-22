from Calculator import square

#To test it yourself
"""
def main():
    test_square()

def test_square():
    for i in range(100):
        try:
            assert(square(i) == i*i)
        except AssertionError:
            print(f"{i} squared is not {i*i}")

if __name__ == "__main__":
    main()
"""

#It is better to divide the test into multiple tests
def test_positive():
    assert(square(2) == 4)
    assert(square(3) == 9)

def test_zero():
    assert(square(0) == 0)
    
def test_negative():
    assert(square(-2) == 4)
    assert(square(-3) == 9)
    