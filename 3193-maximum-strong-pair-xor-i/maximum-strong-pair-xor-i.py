class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j])<=min(nums[i], nums[j]):
                    res.append(nums[i]^nums[j])
        return max(res)
