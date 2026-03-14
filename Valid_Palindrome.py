class Solution(object):
    def isPalindrome(self, s):
        x=""
        for i in s:
            if i.isalnum():
                x+=i
        x=x.lower()
        if x==x[::-1]:
            return True
        else:
            return False
