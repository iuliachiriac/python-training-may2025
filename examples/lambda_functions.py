def compute(a, b, operation):
    return operation(a, b)


def my_sum(a, b):
    return a + b


print(compute(2, 3, pow))
print(compute(7, 2, divmod))
print(compute(5, 7, my_sum))
print(compute(5, 7, lambda a, b: a + b))
