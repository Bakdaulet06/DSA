class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        res = []
        for key, val in d.items():
            if val>1:
                res.append(key)
            if len(res) == 2:
                return res
        return res