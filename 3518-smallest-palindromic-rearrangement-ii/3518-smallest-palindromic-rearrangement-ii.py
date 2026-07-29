from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = {}
        mid = ""
        total = 0

        for c in sorted(cnt):
            half[c] = cnt[c] // 2
            total += half[c]
            if cnt[c] & 1:
                mid = c

        def ways(freq):
            rem = sum(freq.values())
            ans = 1
            for v in freq.values():
                if v:
                    ans *= comb(rem, v)
                    rem -= v
                    if ans >= k:
                        return ans
            return ans

        if ways(half) < k:
            return ""

        left = []

        while total:
            for c in sorted(half):
                if half[c] == 0:
                    continue

                half[c] -= 1
                w = ways(half)

                if w >= k:
                    left.append(c)
                    total -= 1
                    break
                else:
                    k -= w
                    half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]