class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i,j=0,0
        cnt=0
        while j < len(trainers):
            if i<len(players):
                if players[i] <= trainers[j]:
                    cnt+=1
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                break
        return cnt



        return cnt

        