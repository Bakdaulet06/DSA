class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            s = self.to_base(n, i)
            l = 0
            r = len(s) -1
            while(l<r):
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
        return True

    def to_base(self, n, base):
        if n == 0:
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while n > 0:
            result = digits[n % base] + result
            n //= base
        return result
