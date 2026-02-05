function subarraysDivByK(nums: number[], k: number): number {
    const prefixCount = new Map<number, number>()
    prefixCount.set(0, 1)
    let res = 0
    let prefixSum = 0
    for(const num of nums){
        prefixSum+=num
        let remainder = ((prefixSum%k) + k) % k
        if(prefixCount.has(remainder)){
            res+=prefixCount.get(remainder)
        }
        prefixCount.set(remainder, (prefixCount.get(remainder) || 0) + 1)
    }
    return res
};