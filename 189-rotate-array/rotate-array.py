class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a=deque(nums)
        for i in range(k):
            a.appendleft(a[-1])
            a.pop()
        nums[:] = list(a)