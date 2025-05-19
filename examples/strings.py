# multiline_str = """"test" == 'test'
# Out[65]: True"""
# print(multiline_str)
#
# print("She said \"That\'s it.\"\nTest")

name = "jane"
age = 30
height = 1.7

# F-string (Python 3.x)
message = f"{name} is {age} years old"
print(message)

message = f"{name.capitalize()} is {age * 2} years old."
print(message)

message = (f"{name.capitalize():_^15} is {age * 2} years old and has a height"
           f" of {height:.2f} m")
print(message)

# str.format (Python 2.7)
message = "{} is {} years old".format(name, age)
print(message)

message = ("{:_^15} is {} years old and has a height"
           " of {:.2f} m".format(name.capitalize(), age * 2, height))
print(message)
