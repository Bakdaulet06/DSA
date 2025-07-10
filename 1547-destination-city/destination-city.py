class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr = []
        for i in paths:
            arr.append(i[0])
        for i in paths:
            for j in i:
                if j not in arr:
                    return j