class NumArray:

    def __init__(self, nums: List[int]):
        self.prifix_sum=[0]
        for num in nums:
            self.prifix_sum.append(self.prifix_sum[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        left_sum=self.prifix_sum[left]
        right_sum=self.prifix_sum[right+1]

        return right_sum-left_sum


