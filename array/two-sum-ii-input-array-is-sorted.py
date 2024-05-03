class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []