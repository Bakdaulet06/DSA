class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        res = []
        for val in d.values():
            if val not in res:
                res.append(val)
            else:
                return False
        return True