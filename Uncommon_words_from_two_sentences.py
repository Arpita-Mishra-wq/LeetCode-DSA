class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+" "+s2
        l=s.split()
        result=[]
        for i in range(len(l)):
            for j in l[:i]+l[i+1:]:
                if l[i]==j:
                    break
            else:
                result.append(l[i])
        return result
