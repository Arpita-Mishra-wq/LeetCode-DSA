class Solution(object):
    def addToArrayForm(self, num, k):
        s=""
        num1=[]
        for i in num:
            x=str(i)
            s+=x
        s=int(s)
        result=s+k
        for i in str(result):
            num1.append(int(i))
        return num1
