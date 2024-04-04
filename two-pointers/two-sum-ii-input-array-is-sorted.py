class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []