class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                return mid
        return -1 
        