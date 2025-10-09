from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        There are n cities and n-1 edges 
        Each city can reach 0
        imples
        Connected acyclic if undirected
        """

        edges = {(a,b) for a,b in connections} 
        neighbors = {i:[] for i in range(n)}
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        changed = 0
        visitedSet = set()

        def dfs(node):
            nonlocal changed
            if node in visitedSet:
                return 
            visitedSet.add(node)
            for nei in neighbors[node]:
                if nei not in visitedSet and (nei, node) not in edges:
                    changed += 1
                dfs(nei)
                
        dfs(0)
        return changed
        


        