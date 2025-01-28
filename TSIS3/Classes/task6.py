import math
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))

nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_nums = list(filter(is_prime, nums))
print("Prime numbers:", prime_nums)