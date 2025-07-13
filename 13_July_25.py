#Problem 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/editorial

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l = []
        for i in players:
            for j in trainers:
                if (i<=j):
                    l.append(j)
                    trainers.remove(j)
                    break
                else:
                    continue
        return len(l)