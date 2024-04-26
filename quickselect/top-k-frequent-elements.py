class Solution(object):
    def topKFrequent(self, nums, k):
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        sorted_nums = sorted(hashMap, key=hashMap.get, reverse=True)
        return sorted_nums[:k]
        