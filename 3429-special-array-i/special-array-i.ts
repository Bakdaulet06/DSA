function isArraySpecial(nums: number[]): boolean {
    const n: number = nums.length
    if(n===1) return true
    for(let i = 0; i<n-1; i++){
        if(!(nums[i]%2===0&&nums[i+1]%2===1 || nums[i]%2===1 && nums[i+1]%2===0)){
            return false
        }
    }
    return true
};