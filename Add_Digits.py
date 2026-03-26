class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            sum=0
            while num!=0:
                digits=num%10
                sum+=digits
                num//=10
            num=sum
        return num
