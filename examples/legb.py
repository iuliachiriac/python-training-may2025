X = 100


def func(a):
    b = "bb"
    # X = 0  # shadowing
    # sum = 0  # shadowing

    def inner(c):
        d = "dd"
        # a = 7  # shadowing
        print("--- local inner() ---")
        print("Local names:", c, d)
        print("Enclosing names:", a, b, inner)
        print("Global names:", X, func, MyClass)
        print("Built-in names:", None, sum, int)

    inner("cc")

    print("--- local func() ---")
    print("Local names:", a, b, inner)
    print("Global names:", X, func, MyClass)
    print("Built-in names:", None, sum, int)


class MyClass:
    pass


# sum = 0  # shadowing

func("aa")

print("--- global ---")
print("Global names:", X, func, MyClass)
print("Built-in names:", None, sum, int)
