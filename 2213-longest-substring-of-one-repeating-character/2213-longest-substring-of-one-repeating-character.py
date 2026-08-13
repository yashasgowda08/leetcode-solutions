class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        size = 1

        while size < n:
            size *= 2

        tree = [None] * (2 * size)

        def create(c):
            return [c, c, 1, 1, 1, 1]

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]
            length = a[5] + b[5]

            prefix = a[2]
            suffix = b[3]
            best = max(a[4], b[4])

            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                if b[3] == b[5]:
                    suffix = b[5] + a[3]

            return [left_char, right_char, prefix, suffix, best, length]

        for i, c in enumerate(s):
            tree[size + i] = create(c)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(index, c):
            pos = size + index
            tree[pos] = create(c)

            pos //= 2

            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        ans = []

        for c, index in zip(queryCharacters, queryIndices):
            update(index, c)
            ans.append(tree[1][4])

        return ans