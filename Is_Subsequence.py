class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp=s
        for i in t:
            if i not in temp:
                t=t.replace(i,"",1)
            temp=temp.replace(i,"",1)
        if t==s:
            return True
        return False
