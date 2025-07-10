class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = Counter(nums)
        c = 0
        for key, val in d.items():
            if val == 1:
                c+=key
        return c