class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        for key, val in d.items():
            for i in range(0, len(val), key):
                res.append(val[i:i+key])
        return res