import math
import sys
from datetime import date

import functions
# from functions import varargs
# import functions as utils
# from functions import varargs as func_with_var_args
import pypackage.utils_str
# from pypackage import utils_str, utils_math

print(math.sqrt(9), math.pi, math.__file__)

date_obj = date(2009, 5, 8)
print(date_obj)

print(sys.path)

print(functions.decrement(10))
# varargs(1, 2, 3)
# utils.varargs(1, 2)
# func_with_var_args(1, 2)

print(pypackage.VOWELS)
print(pypackage.utils_str)
print(pypackage.utils_str.remove_vowels("hello world"))
print(pypackage.utils_math.circle_area(3))

# print(utils_str.remove_vowels("hello world"))
# print(utils_math.circle_area(10))
