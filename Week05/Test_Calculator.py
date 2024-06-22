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

def test_square():
    assert(square(2) == 4)
    assert(square(3) == 9)
    assert(square(0) == 0)
    assert(square(-2) == 4)
    assert(square(-2) == 9)
    