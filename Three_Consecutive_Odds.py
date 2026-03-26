class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]%2==0:
                arr[i]=0
        s=""
        for i in arr:
            s+=str(i)
        s=s.split("0")
        for i in s:
            if len(i)>=3:
                return True
        return False
