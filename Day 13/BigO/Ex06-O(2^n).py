'''
O(2^n)
'''


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


a = fibonacci(20)
print(a)
