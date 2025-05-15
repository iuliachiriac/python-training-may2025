from functools import wraps


def make_pretty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated", args, kwargs, func)
        return func(*args, **kwargs)
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name1, name2):
    """Greets two people"""
    print(f"Hello, {name1} and {name2}!")


@make_pretty
def decrement(nr, step=1):
    return nr - step


# # Decorating ordinary with @make_pretty is equivalent to:
# ordinary = make_pretty(ordinary)  # ordinary = make_pretty.<locals>.inner
#
# ordinary_dec = make_pretty(ordinary)  # make_pretty.<locals>.inner
# ordinary_dec()
# print(ordinary_dec)

ordinary()
# print(ordinary)

greet("Anna", "John")

result = decrement(10, step=2)
print("decrement result:", result)

print("greet function metadata:", greet, greet.__doc__, greet.__name__)
help(greet)
help(ordinary)
