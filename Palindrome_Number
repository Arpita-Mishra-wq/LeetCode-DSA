class Solution(object):
    def isPalindrome(self, x):
        self.x=x
        org=x
        rev=0
        if rev>-2**31 or rev<2**31-1:
            if x<0:
                return False
            else:
                while x>0:
                    digits=x%10
                    rev=rev*10+digits
                    x//=10
                if rev==org:
                    return True
                return False
