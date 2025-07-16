class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occurace_of_c = []
        result = []

        for i in range(len(s)):
            if s[i] == c:
                occurace_of_c.append(i)

        for i in range(len(s)):
            check=[]
            for j in occurace_of_c:
                check.append(abs(i-j))
            result.append(min(check))

        return result