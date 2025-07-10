class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(list)
        n = len(logs)
        for i in range(n):
            if logs[i][1] not in d[logs[i][0]]:
                d[logs[i][0]].append(logs[i][1])
        res = [0]*k
        lens = []
        for val in d.values():
            lens.append(len(val))
        dlens = Counter(lens)
        for key, val in dlens.items():
            res[key-1] = val
        return res 
              