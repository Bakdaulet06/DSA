function minOperations(s: string): number {
    const arr = s.split("")
    const arr1 = [...arr]
    const arr2 = [...arr]
    const n = s.length
    let min = Infinity
    let count = 0
    let first = arr1[0]
    for(let i = 0; i<n-1; i++){
        const negate = arr1[i] === '0' ? '1' : '0' 
        if(arr1[i] === arr[i+1]){
            arr1[i+1] = negate
            count++
        }
    }
    min = Math.min(min, count)
    count = 1
    arr2[0] = first === '0' ? '1' : '0'
    for(let i = 0; i<n-1; i++){
        const negate = arr2[i] === '0' ? '1' : '0' 
        if(arr2[i] === arr2[i+1]){
            arr2[i+1] = negate
            count++
        }
    }
    return Math.min(min, count)
};