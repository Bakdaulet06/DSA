class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        combined = False
        d = Counter(s)
        curr = ''
        res = []
        d2 = {}
        for i in s:
            if combined:
                res.append(len(curr))
                curr = '' 
            d2[i] = d2.get(i, 0) + 1
            curr+=i
            length = 0
            for key in d2.keys():
                if d2[key] != d[key]:
                    combined = False
                    break
                length+=1
            if length == len(d2):
                combined = True
        res.append(len(curr))
        return res