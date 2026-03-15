class Solution(object):
    def isAnagram(self, s, t):
        sorted_s=str(sorted(s))
        sorted_t=str(sorted(t))
        if sorted_s==sorted_t:
            return True
        return False
