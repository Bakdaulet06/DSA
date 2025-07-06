class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        all_letters = list(string.ascii_lowercase)
        consonants = [letter for letter in all_letters if letter not in vowels]
        v = ''
        c = ''
        maxV = 0
        maxC = 0
        for key, val in Counter(s).items():
            if(key in vowels):
                maxV = max(maxV, val)
            else:
                maxC = max(maxC, val)
        return maxV+maxC