class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=""
        for i in nums:
            s+=str(i)
        l=s.split("0")
        return len(max(l))
