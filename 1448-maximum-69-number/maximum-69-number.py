class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        if '6' not in s:
            return num
        index = s.index('6')
        res = s[0:index]+'9'+s[index+1:]
        return int(res)