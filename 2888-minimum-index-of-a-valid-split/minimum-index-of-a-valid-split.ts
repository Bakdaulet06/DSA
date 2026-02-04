function minimumIndex(nums: number[]): number {
    const map = new Map<number, number>()
    const n = nums.length
    if(n === 1) return -1
    for(const num of nums){
        map.set(num, (map.get(num) || 0) + 1)
    }
    let count = 0
    let max = 0
    let maxKey = 0
    for(const [key, c] of map){
        if(c > max) maxKey = key
        max = Math.max(c, max)
    }
    for(let i = 0; i<n; i++){
        if(nums[i] === maxKey){
            count++
            if(count > Math.floor((i+1)/2) && max - count > Math.floor((n-(i+1))/2)) return i
        }
    }
    return -1
};