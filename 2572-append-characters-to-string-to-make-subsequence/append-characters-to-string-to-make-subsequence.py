class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        c = len(t)
        l = 0
        n = len(s)
        for i in range(n):
            if s[i] == t[l]:
                l+=1
                c-=1
            if c==0:
                return 0
        return c
            