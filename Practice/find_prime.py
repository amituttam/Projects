
def gen_prime(n):
    is_prime = [1 if i > 1 else 0 for i in range(n)]
    for i in range(n):
        if is_prime[i]:
            j = i
            while j < n:
                j += i
                if j < n:
                    is_prime[j] = 0
    return is_prime

for num,prime in enumerate(gen_prime(120)):
    if prime:
        print num,
