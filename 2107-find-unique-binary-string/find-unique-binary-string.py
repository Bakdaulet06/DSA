class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set(nums)
        for i in range(2 ** n):
            b = bin(i)[2:].zfill(n)
            if b not in seen:
                return b
