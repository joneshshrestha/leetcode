def isAnagram1(s: str, t: str):
    s = list(s)
    s.sort()
    t = list(t)
    t.sort()
    if s == t:
        return True
    else:
        return False

def isAnagram2(s: str, t: str):
    if len(s) != len(t):
        return False

    fs, ft = {}, {}
    for i in range(len(s)):
        fs[s[i]] = 1 + fs.get(s[i], 0)
        ft[t[i]] = 1 + ft.get(t[i], 0)
    return fs == ft

print(isAnagram1("anagram", "nagaram"))
print(isAnagram1("rat", "car"))

print(isAnagram2("anagram", "nagaram"))
print(isAnagram2("rat", "car"))