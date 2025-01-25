def topKFrequent1(nums, k):
    output = {}
    
    for num in nums:
        output[num] = output.get(num, 0) + 1
    
    arr = []

    for n, c in output.items():
        arr.append([c, n]) # to sort by frequency
    arr.sort()

    res = []
    for i in range(k):
        print('hello')
        res.append(arr.pop()[1]) # arr.pop() pops the last array from the sorted array
    return res

def topKFrequent2(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)] #[[], [], ...]

    for n in nums:
        count[n] = 1 + count.get(n, 0) # count = {num: frequency}

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    
print(topKFrequent1([1,2,2,3,3,3], 2))
print(topKFrequent2([1,2,2,3,3,3], 2))