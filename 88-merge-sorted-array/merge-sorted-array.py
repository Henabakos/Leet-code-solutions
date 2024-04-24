class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return nums1

        for i in range(n):
            nums1[m]=nums2[i]
            m+=1
        nums1.sort()
        return nums1