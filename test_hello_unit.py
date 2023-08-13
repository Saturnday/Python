from hello_unit import say_hello

#seporated the test function for different scenarios
    
def test_argument():
    assert say_hello("mike") == "Hello, mike"

def test_default():
    assert say_hello() == "Hello, world"

def test_several_arguments():
    for _ in ["Name1", "0", "!@#$"]:
        assert say_hello(_)==f"Hello, {_}"
#to treat folder as a package create a file called __init__.py
#to create a folder in cmd run "mkdr name_of_the_foder" eg: code test/__init__.py  (test is a name of a folder)
#to create a file in this folder eg: code test/test_hello.py
#packages - python modules that are organized in a folder