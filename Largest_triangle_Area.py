class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area=[]
        for i in points:
            for j in points:
                for k in points:
                    x1,y1=i
                    x2,y2=j
                    x3,y3=k
                    area.append(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
        return max(area)
