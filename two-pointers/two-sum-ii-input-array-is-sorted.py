class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return (left + 1, right + 1)
        return []