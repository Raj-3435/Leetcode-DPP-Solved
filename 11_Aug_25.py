# Problem 2438. Range Product Queries of Powers

class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7   #important for large testcases 
        powers = []
        res = []

        bits = [int(b) for b in bin(n)[2:]][::-1]

        x = 0
        for p in bits:
            if p == 1:
                powers.append(2 ** x)
            x += 1

        for m in queries:
            data = 1
            for k in range(m[0], m[-1] + 1):
                data = (data * powers[k]) % MOD
            res.append(data)

        return res
