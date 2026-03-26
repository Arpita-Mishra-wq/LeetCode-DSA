class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=""
        for i in s:
            if i in "aeiouAEIOU":
                s=s.replace(i,"_")
                vow+=i
        for i in vow[::-1]:
            s=s.replace("_",i,1)
        return s
