
def reverse(a):
    b = [] 
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])

    return ''.join(b)

a = "rolling"
b = a[::-1]
c = reverse(a)

print a,b,c
