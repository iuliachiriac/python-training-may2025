from functools import wraps


def make_pretty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"I am decorating `{func.__name__}` which was called with "
              f"args={args} and kwargs={kwargs}")
        return func(*args, **kwargs)

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")

# Decorating with @ is equivalent to:
# ordinary = make_pretty(ordinary)  # make_pretty.<locals>.inner


@make_pretty
def greet(name):
    """Prints a greeting for name"""
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=1):
    return nr - step


ordinary()  # make_pretty.<locals>.inner()
greet("Anna")  # make_pretty.<locals>.inner("Anna")
print("Result =", decrement(10, 2))
print("Result =", decrement(nr=10, step=2))  # make_pretty.<locals>.inner(nr=10, step=2)

print(greet, greet.__name__, greet.__doc__)
print(decrement, ordinary)
