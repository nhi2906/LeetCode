class Solution(object):
    def characterReplacement(self, s, k):
        # set up 
        left = 0
        count = {}
        max_freq = 0
        # get the count 
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
        return (right - left + 1) 
        
        