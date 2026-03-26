class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters=""
        for i in s:
            if i.isalpha()==True:
                letters+=i
                s=s.replace(i,"\\")
        for i in letters[::-1]:
            s=s.replace("\\",i,1)
        return s
