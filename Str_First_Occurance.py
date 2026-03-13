class Solution(object):
    def strStr(self, haystack, needle):
        self.haystack=haystack
        self.needle=needle
        if 1 <= len(haystack)<= 10**4 and 1 <=len(needle) <= 10**4 and haystack==haystack.lower() and needle==needle.lower():
            return haystack.find(needle)
