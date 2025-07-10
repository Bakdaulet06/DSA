class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(n):
            for j in range(i, n):
                d = set(nums[i:j+1])
                s+=(len(d)*len(d))
        return s
