import re


pattern = r"((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])"  # raw string
text = "Hello john.doe@gmail.com!"

match_obj = re.search(pattern, text)
print(match_obj.group(), match_obj.groups(), match_obj.span())

text = "print(match_obj.group(), match_obj.groups(), match_obj.span())"
words = [word for word in re.split(r"[()\., ]", text) if word]
print(words)
