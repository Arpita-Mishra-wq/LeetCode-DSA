class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        div_score=[]
        divisors.sort()
        for i in divisors:
            count=0
            for j in nums:
                if j%i==0:
                    count+=1
            div_score.append(count)
        result=div_score.index(max(div_score))
        return divisors[result]
        
