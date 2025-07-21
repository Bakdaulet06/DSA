class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            start = max(0, i-nums[i])
            s = sum(nums[start:i+1])
            total+=s
        return total