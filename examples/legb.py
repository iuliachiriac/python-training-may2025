X = 100


def func(a):
    b = "b"
    # sum = 0  # shadowing of built-in name
    # global X  # use global keyword to use global variable (and modify it)
    # X = 0  # shadowing of global name

    def inner(c):
        d = "d"
        # nonlocal a
        # a = "test"
        # X = "test"
        print("--- local inner() ---")
        print("Local names:", c, d)
        print("Enclosing names:", a, b, inner)
        print("Global names:", X, func, MyClass)
        print("Built-in names:", sum, min, list, dict, end="\n\n")

    inner("c")

    print("--- local func() ---")
    print("Local names:", a, b, inner)
    print("Global names:", X, func, MyClass)
    print("Built-in names:", sum, min, list, dict, end="\n\n")


class MyClass:
    pass


# Shadowing of built-in names (should be avoided)
# list = []
# def min(x, y):
#     return x

func("a")

print("--- global ---")
print("Global names:", X, func, MyClass)
print("Built-in names:", sum, min, list, dict)
