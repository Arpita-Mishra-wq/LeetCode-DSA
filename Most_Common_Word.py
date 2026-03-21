class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in paragraph:
            if i.isalpha()!=True and i!=" ":
                paragraph=paragraph.replace(i," ")
        paragraph=paragraph.lower()
        words=paragraph.split()
        l=[]
        for i in words:
            if i not in banned:
                l.append(i)
        return mode(l)
