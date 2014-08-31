
def find_prime(n):
    is_prime = [1 if i > 1 else 0 for i in range(n)]
    for i in range(2,n):
        if is_prime[i]:
            j = i
            while j < n:
                j += i
                if j < n:
                    is_prime[j] = False
    return is_prime

is_prime = find_prime(100)
print([i for i in range(100) if is_prime[i] == True])
