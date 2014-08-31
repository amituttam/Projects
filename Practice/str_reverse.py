
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        r = ""
        for i in range(len(s)-1,-1,-1):
            r += s[i]
        return r

print(reverse("test"))
print(reverse("amit"))
