class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        l = 0
        r = 0
        minN = min(len(players), len(trainers))
        n = len(players)
        c = 0
        while(l<n):
            if players[l]<=trainers[r]:
                c+=1
                r+=1
                l+=1
            else:
                r+=1
            if r == len(trainers):
                break
        return c
            
            
