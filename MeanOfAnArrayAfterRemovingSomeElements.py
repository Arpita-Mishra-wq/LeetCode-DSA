class Solution:
    def trimMean(self, arr: List[int]) -> float:
        total=0
        arr.sort()
        rmv=(len(arr)*5)//100
        arr=arr[rmv:len(arr)-rmv]
        for i in arr:
            total+=i
        return total/len(arr)
