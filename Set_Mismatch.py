class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing=i
            if freq[i]==2:
                duplicate=i
        return [duplicate,missing]
