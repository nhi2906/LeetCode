# method: 
# - count the number of each character in both string
# - use the hashMap

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        countT = {}
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        