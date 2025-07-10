class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = Counter(s)
        ch = d[s[0]]
        for key, val in d.items():
            if ch != val:
                return False
        return True