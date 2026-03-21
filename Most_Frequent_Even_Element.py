class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even=[]
        for i in nums:
            if i%2==0:
                even.append(i)
        count=0
        even.sort()
        if not even:
            return -1
        return mode(even)
