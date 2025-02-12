def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

N = 10
for num in square_generator(N):
    print(num, end=" ")
