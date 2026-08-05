from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)
            rev[v].append(u)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)

        for v in range(n):
            if suspicious[v]:
                for u in rev[v]:
                    if not suspicious[u]:
                        return list(range(n))

        return [i for i in range(n) if not suspicious[i]]