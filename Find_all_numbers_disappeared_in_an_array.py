class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        x=set(nums)
        for i in range(1,len(nums)+1):
            if i not in x:
                result.append(i)
        return result
