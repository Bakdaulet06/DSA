from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            subarray = sorted(nums[l[i]:r[i]+1])  # Also make sure you include r[i], not exclude
            if self.checkBool(subarray):
                res.append(True)
            else:
                res.append(False)
        return res
    
    def checkBool(self, nums: List[int]) -> bool:
        diff = nums[1] - nums[0]
        for i in range(1, len(nums)-1):
            if diff != nums[i+1] - nums[i]:
                return False
        return True
