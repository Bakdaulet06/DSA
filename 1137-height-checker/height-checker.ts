function heightChecker(heights: number[]): number {
    const expected = [...heights]
    expected.sort((a, b) => a - b)
    const n = heights.length
    let count = 0
    for(let i = 0; i<n; i++){
        if(expected[i] !== heights[i]) count++
    }
    return count
};
