class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dfs(i, m):
            if i >= n:
                return 0

            if 2 * m >= n - i:
                return suffix[i]

            if (i, m) in memo:
                return memo[(i, m)]

            best = 0

            for x in range(1, 2 * m + 1):
                best = max(
                    best,
                    suffix[i] - dfs(i + x, max(m, x))
                )

            memo[(i, m)] = best
            return best

        return dfs(0, 1)