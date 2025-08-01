class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        res = []
        res.append([1])
        res.append([1,1])
        for i in range(3, numRows+1):
            curr = [1]
            for j in range(1, i-1):
                curr.append(res[i-2][j-1]+res[i-2][j])
            curr.append(1)
            res.append(curr)
        return res
