class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l = 0
        r = len(nums)-1
        n = len(nums)
        for i in range(n):
            if nums[i]%2==1:
                res[r] = nums[i]
                r-=1
            else:   
                res[l] = nums[i]
                l+=1
        return res