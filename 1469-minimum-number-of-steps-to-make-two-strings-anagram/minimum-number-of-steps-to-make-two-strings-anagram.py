class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dt = Counter(t)
        c = 0
        for i in sorted(s):
            if i not in dt.keys():
                c+=1
            else:
                if dt[i]>0:
                    dt[i] = dt[i]-1
                else:
                    c+=1
        return c