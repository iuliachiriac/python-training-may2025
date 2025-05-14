import math
import sys
from datetime import date, timedelta

import string_processing
import pypackage


print(globals())
print(math.sqrt(9), math.pi)

date_obj = date(2018, 6, 2)
print(date_obj + timedelta(days=4))

print(sys.path)

print(string_processing.VOWELS)
result = string_processing.remove_vowels("hello world")
print(result)

pypackage.get("https://docs.python.org/3/library/datetime.html")

# from pypackage import utils
# utils.do_something()
