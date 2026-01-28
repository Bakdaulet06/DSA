function destCity(paths: string[][]): string {
    const arr: string[] = []
    for(const a of paths){
        arr.push(a[0])
    }
    for(const a of paths){
        if(!arr.includes(a[1])) return a[1]
    }
};