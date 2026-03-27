class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        for i in range(n):
            if i%2==0:
                if n//2>=len(list(set(candyType))):
                    return len(list(set(candyType)))
                return n//2
