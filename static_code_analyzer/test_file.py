import os
import sys

class MyClass:
    """This is a docstring."""
    def __init__(self):
        pass

def my_function(a, b, c, d, e, f, g, h, i, j, k, l):
    """This is a docstring."""
    x = 1 # Unused variable
    pass

def another_function():
    """This is a docstring."""
    print("Hello, world!")
    # TODO: Implement something here
    pass

def function_without_docstring():
    # FIXME: This needs to be fixed
    y = 2
    pass

print("This is a very long line that will definitely exceed the maximum line length that we have set for our static analyzer and should be flagged as an issue by the linter")