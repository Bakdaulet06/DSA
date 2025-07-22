class Solution:
    def reformatNumber(self, number: str) -> str:
        combined = ''
        for i in range(len(number)):
            if number[i] != '-' and number[i] != ' ':
                combined+=number[i]
        l = len(combined)
        res = ''
        if l<3:
            return combined
        for i in range(0, l, 3):
            if l - i == 4:
                res+=combined[i:i+2]
                res+='-'
                res+=combined[i+2:i+4]
                break
            res+=combined[i:i+3]
            if i+3 != l and i+3<l:
                res+='-'
        return res