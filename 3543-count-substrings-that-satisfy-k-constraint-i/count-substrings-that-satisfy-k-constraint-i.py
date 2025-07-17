class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        c = 0
        while(l<=n):
            for i in range(n-l):
                sub = s[i:i+l+1]
                d = Counter(sub)
                if d['0'] <= k or d['1']<=k:
                    c+=1
            l+=1
        return c
