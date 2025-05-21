# from pypackage import VOWELS  # absolute import
from . import VOWELS  # relative import


def remove_vowels(text):
    result = ""
    for char in text:
        if char not in VOWELS:
            result += char
    return result
