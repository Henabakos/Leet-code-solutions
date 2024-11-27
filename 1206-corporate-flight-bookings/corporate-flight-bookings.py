class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffArr = [0]*(n+1)
        for start, end, seat in bookings:
            diffArr[start-1] += seat
            diffArr[end] -= seat
        for i in range(1,n):
            diffArr[i] += diffArr[i-1]
        return diffArr[:n]