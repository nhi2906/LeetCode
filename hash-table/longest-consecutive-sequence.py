class Solution(object):
    def longestConsecutive(self, nums):
        longest = 0 
        hashSet = set(nums)
        for num in nums:
            if (num - 1) not in hashSet:
                length = 0
                while (num + length) in hashSet:
                    length += 1
                longest = max(length, longest)
        return longest