class Solution:
    def knightDialer(self, n: int) -> int:
        dp = {0: (4, 6), 1: (8, 6), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9),
              5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
        m = {}

        def knight(size, val):
            if size == 0:
                return 1
            if (size, val) in m:
                return m[(size, val)]
            count = 0
            for ele in dp[val]:
                count += knight(size-1, ele)
            m[(size, val)] = count
            return count

        res = 0
        for i in range(10):
            res += knight(n-1, i)
        return res % 1000000007
