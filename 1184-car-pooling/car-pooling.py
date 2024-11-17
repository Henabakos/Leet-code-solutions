class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0 for _ in range(1001)]
        for trip in trips:
            stops[trip[1]] += trip[0]
            stops[trip[2]] -= trip[0]

        index = 0

        while capacity >= 0 and index < 1001:
            capacity -= stops[index]
            index += 1
        return capacity >= 0