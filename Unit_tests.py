"""
from calculator import square

def main():
    test_square()

def test_square():
    if square(3) != 9:
        print("square(3) was not 9")
    if square(0) != 0:
        print("square(0) was not 0")
    if square(-5) != 25:
        print("square(-5) was not 25")

if __name__ == "__main__":
    main()
"""

#using assert and try/except
"""
from calculator import square
def main():
    test_square()
def test_square():
    try:
        assert square(3) == 9 #will output AssertionError if not true
    except:
        print("square(3) was not 9")
    try:
        assert square(0) == 0
    except:
        print("square(0) was not 0")
    try:
        assert square(-5) == 25
    except:
        print("square(-5) was not 25")

if __name__ == "__main__":
    main()
"""

#here i installed pytest and used it to test the function:
#pytest is a library that allows you to test your code
#unit testing is a way to test your code in small pieces/ test each function/test every UNIT of code

from calculator import square
#dont need ot import pytest because it is already installed
def test_square():
    assert square(3) == 9
    assert square(0) == 0
    assert square(-5) == 25
    assert square(2) == 4
#to run this test, go to terminal and type: pytest unit_tests.py
