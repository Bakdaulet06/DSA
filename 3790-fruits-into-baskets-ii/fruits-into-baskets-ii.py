class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        c = 0
        for i in range(n):
            n2 = len(baskets)
            placed = False
            for j in range(n2):
                if fruits[i]<=baskets[j]:
                    baskets.pop(j)
                    placed = True
                    break
            if not placed:
                c+=1
        return c
