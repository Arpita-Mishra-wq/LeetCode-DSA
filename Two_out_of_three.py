class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                result.append(i)
        for i in nums2:
            if i in nums1 or i in nums3:
                result.append(i)
        return (list(set(result)))
