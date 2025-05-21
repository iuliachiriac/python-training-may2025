def string_concat(input_str):
    print("input_str id before +=", id(input_str))
    input_str += "test"  # input_str = input_str + "test"
    print("input_str id after +=", id(input_str))


def list_concat(input_list):
    print("input_list id before +=", id(input_list))
    input_list += ["test"]
    print("input_list id after +=", id(input_list))


def modify(x):
    x += 5
    return x


my_str = "hello world "
my_list = ["hello", "world"]
my_int = 10

print("Before concat:", my_str, id(my_str))
string_concat(my_str)
print("After concat:", my_str)

print("Before concat:", my_list, id(my_list))
list_concat(my_list)
print("After concat:", my_list)

print("Before modify:", my_int)
result = modify(my_int)
print("After modify:", my_int)
print("Result modify:", result)
# print(x)
