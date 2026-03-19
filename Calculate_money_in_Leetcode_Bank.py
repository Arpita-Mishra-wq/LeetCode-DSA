class Solution:
    def totalMoney(self, n: int) -> int:
        monday=1
        weeks=n//7
        days=n%7
        bank=0
        for i in range(weeks):
            for j in range(monday,monday+7):
                bank+=j
            monday+=1
        for i in range(monday,monday+days):
            bank+=i
        return bank
