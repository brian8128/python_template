from __future__ import absolute_import, division, print_function

from subpackage.library import function_A
from settings import *

if __name__ == "__main__":
    print("Running my_script")
    function_A()
    print(CONSTANT)
    print(STRING)