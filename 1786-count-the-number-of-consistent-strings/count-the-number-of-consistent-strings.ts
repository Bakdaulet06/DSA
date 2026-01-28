function countConsistentStrings(allowed: string, words: string[]): number {
    let count: number = 0
    for(let i = 0; i<words.length; i++){
        let consistent = true
        for(let j = 0; j<words[i].length; j++){
            if(!allowed.includes(words[i][j])){
                consistent = false
                break
            }
        }
        if(consistent) count++
    }
    return count
};