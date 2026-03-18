class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k=None
        if ch in word:
            for i in range(len(word)):
                if word[i]==ch:
                    k=i+1
                    break
            return word[:k][::-1]+word[k::]
        return word
