class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        sum=0
        for i in s:
            if i=='|':
                count+=1
            if count%2==0 and i=='*':
                sum+=1
        return sum
