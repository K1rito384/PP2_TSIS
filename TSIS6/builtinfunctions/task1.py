def multiply_list(numbers):
    from functools import reduce
    return reduce(lambda x, y: x * y, numbers)