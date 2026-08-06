from itertools import count

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in count(n):
            product = 1
            for d in str(num):
                product *= int(d)
            if product % t == 0:
                return num