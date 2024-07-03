class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coordinate = []
        for i in range(len(points)):
            x_coordinate.append(points[i][0])
        x_coordinate.sort()

        sum1 = 0
        for i in range(1,len(x_coordinate)):
            sum1 = max(sum1,abs(x_coordinate[i] - x_coordinate[i-1]))
        
        return sum1