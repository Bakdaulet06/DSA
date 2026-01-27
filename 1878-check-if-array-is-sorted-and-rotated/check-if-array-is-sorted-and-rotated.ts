function check(nums: number[]): boolean {
    let l = 0
    const n = nums.length
    for(let i = 0; i<n-1; i++){
        if(nums[i] > nums[i+1]){
            l = i + 1
            break
        }
    }
    const part1 = nums.slice(l, n)
    const part2 = nums.slice(0, l)
    const newArr = [...part1, ...part2]
    const sorted = [...nums].sort((a, b) => a - b)
    for(let i = 0; i<n; i++){
        if(newArr[i] !== sorted[i]) return false
    }
    return true
};