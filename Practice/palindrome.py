
def is_pal(s):
    if len(s) <= 1:
        return True
    else:
        return (s[0] == s[len(s)-1]) and is_pal(s[1:len(s)-1])

print(is_pal("kayak"))
print(is_pal("racecar"))
print(is_pal("rope"))

nums = [str(i) for i in range(1,10000)]
print(sum(map(is_pal,nums)))
