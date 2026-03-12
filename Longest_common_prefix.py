class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        last=words[-1]
        return len(last)
