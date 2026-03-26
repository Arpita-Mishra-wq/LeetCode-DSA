class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        count=0
        for i in range(len(str(num))):
            digit=temp%10
            temp//=10
            if num%digit==0:
                count+=1
        return count
