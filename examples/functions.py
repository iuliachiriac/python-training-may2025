def my_function(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs), end="\n\n")


my_function()
my_function(10)
my_function(10, 20, 30)

my_function(name="Ana", age=10)
my_function(10, 20, 30, name="Ana", job="developer")

lst = ["Jane", 20]
my_function(lst)  # my_function(["Jane", 20])
my_function(*lst)  # my_function("Jane", 20)

dct = {"name": "Jane", "age": 20}
my_function(dct)  # my_function({"name": "Jane", "age": 20})
my_function(*dct)  # my_function("name", "age")
my_function(**dct)  # my_function(name="Jane", age=20)
