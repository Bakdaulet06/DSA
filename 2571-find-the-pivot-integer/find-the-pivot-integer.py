class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        sums = []
        prev = 0
        for i in range(1, n+1):
            prev+=i
            sums.append(prev)
        s = len(sums)
        l = sums[s-1]
        for i in range(s):
            if l - sums[i] + (i+1) == sums[i]:
                return i+1
        return -1