def polin(s):
    l = len(s)
    m = ' ,-?!'
    for j in m:
        s = s.replace(j, '')
    s = s.lower()
    k = s[::-1]
    if s != k:
        return "Nie palindrom =("
    return "Palindrom =)"

print(polin('Elle'))
print(polin('Xano'))
print(polin('Natan'))
print(polin('Noyon'))
print(polin('Otta'))
