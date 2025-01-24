from collections import defaultdict

def groupAnagrams1(strs):
    output = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        output[sortedS].append(s)
    return list(output.values())

def groupAnagrams2(strs):
    output = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            pos = (ord(c) - ord('a'))
            count[pos] += 1
        output[tuple(count)].append(s)
    return list(output.values())

print(groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]