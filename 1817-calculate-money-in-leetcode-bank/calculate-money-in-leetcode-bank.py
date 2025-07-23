class Solution:
    def totalMoney(self, n: int) -> int:
        c = 0
        l = 0
        while(n!=0):
            for i in range(1, 8):
                c+=(i+l)
                n-=1
                if n == 0:
                    return c
            l+=1
        return c 