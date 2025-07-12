#Problem 1900 : The Earliest and Latest Rounds Where Players Compete
#https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/editorial

from functools import lru_cache
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dfs(players, round_no):
            players = tuple(sorted(players))
            i,j = 0, len(players)-1

            while i<j:
                a,b = players[i], players[j]
                if (a==firstPlayer and b==secondPlayer) or (a == secondPlayer and b==firstPlayer):
                    return [round_no, round_no]
                i+=1
                j-=1

            next_states = set()

            def gen(i,j,next_round):
                if i>j:
                    yield tuple(sorted(next_round))
                    return 
                if i==j:
                    yield from gen(i+1,j-1,next_round+[players[i]])
                    return 
                
                a,b = players[i], players[j]

                if {a,b}=={firstPlayer, secondPlayer}:
                    pass
                elif a in {firstPlayer, secondPlayer}:
                    yield from gen(i+1, j-1, next_round+[a])
                elif b in {firstPlayer, secondPlayer}:
                    yield from gen(i+1, j-1, next_round+[b])
                else:
                    yield from gen(i+1,j-1,next_round+[a])
                    yield from gen(i+1,j-1,next_round+[b])
                
            min_round = float('inf')
            max_round = 0

            for next_players in gen(0, len(players)-1,[]):
                e, l = dfs(next_players, round_no + 1)
                min_round = min(min_round,e)
                max_round = max(max_round,l)

            return [min_round, max_round]

        return dfs(tuple(range(1,n+1)),1)