class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.capitalize()==word or word.lower()==word or word.upper()==word:
            return True
        return False
