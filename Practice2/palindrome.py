
def is_pal(s):
    return s == s[::-1]

def is_pal_rec(s):
    if len(s) == 1:
        return True
    else:
        return (s[0] == s[-1]) and is_pal_rec(s[1:-1])

print(is_pal("kayak"))
print(is_pal_rec("kayak"))
