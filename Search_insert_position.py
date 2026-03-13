class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        nums.append(target)
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
