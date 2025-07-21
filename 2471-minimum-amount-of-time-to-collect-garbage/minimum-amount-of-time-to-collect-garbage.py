class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        n = len(garbage)
        ch = ''
        def summer(ch: str) -> int:
            c = 0
            for j in range(n-1, -1, -1):
                if ch in garbage[j]:
                    if j != 0:
                        c = sum(travel[0:j])
                    for k in range(j+1):
                        c+=garbage[k].count(ch)
                    break
            return c
        ch = ['M', 'P', 'G']
        for c in ch:
            total+=summer(c)
        return total
    
    

