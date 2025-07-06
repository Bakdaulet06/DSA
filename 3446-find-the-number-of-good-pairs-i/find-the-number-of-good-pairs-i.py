class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        c = 0
        for i in range(n):
            for j in range(m):
                if nums1[i]%(nums2[j]*k)==0:
                    c+=1
        return c