class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            rev_pos = 26 - (ord(s[i]) - ord('a'))
            result += (i + 1) * rev_pos
        return result
