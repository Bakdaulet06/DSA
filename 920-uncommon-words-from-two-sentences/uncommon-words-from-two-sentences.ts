function uncommonFromSentences(s1: string, s2: string): string[] {
    const s3 = s1 + " " + s2
    const words: string[] = s3.split(" ")
    const count: Record<string, number> = {}
    for(const word of words){
        count[word] = (count[word] || 0) + 1
    }
    const res: string[] = []
    for(const word in count){
        if(count[word] === 1) res.push(word)
    }
    return res
};