class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        n = len(digits)
        
        def backtrack(idx, comb):
            if idx == n:
                res.append(comb[:])
                return
            for letter in d[digits[idx]]:
                backtrack(idx+1, comb+letter)
        
        backtrack(0, '')
        return res