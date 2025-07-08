class Solution:
    def romanToInt(self, s: str) -> int:
        res = []
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if len(s) == 1:
            return roman[s[0]]
        n = len(s)
        prev = 0
        final = []
        for i in range(0, n):
            curr = roman[s[i]]
            if prev == 1 and curr == 10:
                curr = 9
            elif prev == 1 and curr == 1:
                curr = 2
            elif prev == 2 and curr == 1:
                curr = 3
            elif prev == 5 and curr == 1:
                curr = 6
            elif prev == 6 and curr == 1:
                curr = 7
            elif prev == 7 and curr == 1:
                curr = 8
            elif prev == 1 and curr == 5:
                curr = 4
            elif prev == 10 and curr == 100:
                curr = 90
            elif prev == 10 and curr == 50:
                curr = 40
            elif prev == 10 and curr == 10:
                curr = 20
            elif prev == 20 and curr == 10:
                curr = 30
            elif prev == 50 and curr == 10:
                curr = 60
            elif prev == 60 and curr == 10:
                curr = 70
            elif prev == 70 and curr == 10:
                curr = 80
            elif prev == 100 and curr == 1000:
                curr = 900
            elif prev == 100 and curr == 500:
                curr = 400
            elif prev == 100 and curr == 100:
                curr = 200
            elif prev == 200 and curr == 100:
                curr = 300
            elif prev == 500 and curr == 100:
                curr = 600
            elif prev == 600 and curr == 100:
                curr = 700
            elif prev == 700 and curr == 100:
                curr = 800
            elif prev == 1000 and curr == 1000:
                curr = 2000
            elif prev == 2000 and curr == 1000:
                curr = 3000
            prev = curr
            res.append(curr)
        for i in range(len(res)-1):
            if len(str(res[i])) != len(str(res[i+1])):
                final.append(res[i])
            if i == len(res)-2:
                final.append(res[i+1])
        return sum(final)

            
            



        