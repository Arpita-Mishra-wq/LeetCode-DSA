class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result=[]
        for ch in words[0]:
            for i in range(1,len(words)):
                if ch not in words[i]:
                    break
                else:
                    words[i]=words[i].replace(ch,"",1)
            else:
                result.append(ch)
        return result
