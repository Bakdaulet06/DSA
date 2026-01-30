function averageWaitingTime(customers: number[][]): number {
    const n = customers.length
    let allTime = customers[0][1]
    let queue = customers[0][0] + customers[0][1]
    for(let i = 1; i<n; i++){
        const came = customers[i][0]
        const wait = customers[i][1]
        if(came>=queue){
            allTime+=wait
            queue = (came+wait)
            continue
        }
        queue+=wait
        allTime+=(queue-came)
    }
    return allTime/n
};