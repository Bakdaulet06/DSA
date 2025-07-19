class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            sub = nums[i:i+3]
            if len(sub)!=3:
                return -1
            for j in range(i, i+3):
                if nums[j] == 0:
                    nums[j] = 1
                else:
                    nums[j] = 0
            c+=1
        return c    
    

        