
letters = ["I", "V","X", "L", "C", "M"]
vals = [1,5,10,50,100,1000]
lookup = dict(zip(letters,vals))

def get_roman_val(s):
    if len(s) == 1:
        return lookup[s]
    else:
        sums = 0
        while s:
            if len(s) == 1 or lookup[s[0]] >= lookup[s[1]]:
                sums += lookup[s[0]]
                s = s[1:]
            else:
                sums += lookup[s[1]] - lookup[s[0]]
                s = s[2:]
        return sums

print(get_roman_val("VC"))

