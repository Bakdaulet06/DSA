class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            reverse = ''
            for i in range(len(s)-1, -1, -1):
                reverse+=s[i]
            nums.append(int(reverse))
        return len(Counter(nums))
