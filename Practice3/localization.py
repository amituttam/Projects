
from pprint import pprint

numeronyms = {}

def gen_numeronym(lang):
    if len(lang) < 3:
        return lang

    numeronym = "%s%d%s" % (lang[0], len(lang[1:-1]), lang[-1])
    if numeronym not in numeronyms:
        numeronyms[numeronym] = lang

    return numeronym

print(gen_numeronym("localization"))
print(gen_numeronym("international"))
print(gen_numeronym("l1111111111n"))

pprint(numeronyms)
