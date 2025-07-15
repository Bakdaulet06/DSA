class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if self.isPalindrome(s):
            return 1
        return 2
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        while(l<r):
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True