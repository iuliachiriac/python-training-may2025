"""Functions for processing strings"""


VOWELS = "aeiou"
VOWELS += VOWELS.upper()


def remove_vowels(text):
    for vowel in VOWELS:
        text = text.replace(vowel, "")
    return text


def get_longer_words(*words, n=-1):
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return long_words


# print(__name__)
if __name__ == "__main__":  # if current file is executed
    with_vowels = "argument string vowelAA"
    print(f'String "{with_vowels}" without vowels: '
          f'{remove_vowels(with_vowels)}.')

    print(get_longer_words("hello", "hi", "bye", n=2))
