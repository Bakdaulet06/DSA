class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        d = defaultdict(list)
        c = 0
        for i in range(0, n, 2):
            if rings[i] not in d[rings[i+1]]:
                d[rings[i+1]].append(rings[i])
        for vals in d.values():
            if len(vals) == 3:
                c+=1
        return c