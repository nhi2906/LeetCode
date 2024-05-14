class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum > target:
                right -= 1
            elif twoSum < target:
                left += 1
            else:
                return (left + 1, right + 1)
        return -1 
        