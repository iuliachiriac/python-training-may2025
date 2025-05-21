import math


def my_function(x: int):  # type hint
    return x, x+1


def decrement(nr, step=1):
    return nr - step


def varargs(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs), end="\n\n")


def some_func(x):
    return math.sqrt(x) * 3


# print(f"inside functions.py, __name__ = {__name__}")
if __name__ == "__main__":
    print(my_function(10))
    print(my_function(5.3))

    print(decrement(10))
    print(decrement(10, 2))  # positional arguments
    print(decrement(nr=10, step=2))  # keywords arguments
    print(decrement(10, step=2))

    varargs()
    varargs(10)
    varargs(10, 20, 30)

    varargs(name="Jane", age=20)
    varargs(1, 2, 3, name="Jane", age=20)

    l = [4, 6, 1, 7]
    varargs(l)  # call varargs with one argument
    varargs(*l)  # call varargs with len(l) arguments

    d = {"name": "Anna", "age": 30}
    varargs(d)
    varargs(**d)
