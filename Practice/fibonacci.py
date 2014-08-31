
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibs = [fibonacci(n) for n in range(0,20)]
print fibs
