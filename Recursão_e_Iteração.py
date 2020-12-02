import time


def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n + 1):
        res = a + b
        a, b = b, res
    return res

m = dict()
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
        return m[n]

n = 35
start = time.time()
print(fib_rec(n))
print(f'Recursive: {time.time() - start} seconds.')
start = time.time()
print(fib_it(n))
print(f'Iteractive: {time.time() - start} seconds.')
start = time.time()
print(fib_mem(n))
print(f'Memorization: {time.time() - start} seconds.')
