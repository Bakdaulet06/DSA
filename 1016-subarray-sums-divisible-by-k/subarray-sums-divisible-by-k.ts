function subarraysDivByK(nums: number[], k: number): number {
    const prefixSums = new Map<number, number>()
    let res = 0
    let curSum = 0
    prefixSums.set(0, 1)
    for(const num of nums){
        curSum+=num
        const remainder = ((curSum%k)+k)%k
        if(prefixSums.has(remainder)){
            res+=prefixSums.get(remainder)
        }
        prefixSums.set(remainder, (prefixSums.get(remainder) || 0)+1)
    }
    return res
};