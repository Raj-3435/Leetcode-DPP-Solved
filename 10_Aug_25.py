class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        count_n = Counter(str(n))
        return any(count_n == Counter(str(1 << i)) for i in range(31))
