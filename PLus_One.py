class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in range(len(digits)):
            num=num*10+digits[i]
        result=num+1
        l=[]
        while result>0:
            digit=result%10
            l.append(digit)
            result=result//10
        return l[::-1]
