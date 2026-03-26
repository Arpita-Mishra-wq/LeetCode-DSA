class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        result=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    d[list1[i]]=i+j
        minimum=min(d.values())
        for k,v in d.items():
            if v==minimum:
                result.append(k)
        return result
