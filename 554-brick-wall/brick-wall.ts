function leastBricks(wall: number[][]): number {
    let entryPoints: Record<number, number> = {}
    for(const row of wall){
        let pos = 0
        for(let i = 0; i<row.length-1; i++){
            pos+=row[i]
            if(entryPoints[pos]){
                entryPoints[pos] = entryPoints[pos] + 1
            }else{
                entryPoints[pos] = 1
            }
        }
    }
    console.log(entryPoints)
    const values = Object.values(entryPoints)
    const max = values.length ? Math.max(...values) : 0
    return wall.length - max
};