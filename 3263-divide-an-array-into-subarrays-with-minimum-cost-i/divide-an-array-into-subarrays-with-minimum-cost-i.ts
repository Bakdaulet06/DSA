function minimumCost(nums: number[]): number {
    let sum = nums[0]
    let arr = nums.slice(1).sort((a, b) => a-b)
    sum+=arr[0]+arr[1]
    return sum
};