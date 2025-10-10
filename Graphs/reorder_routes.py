from typing import List
from collections import deque
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
        bfs_queue = deque()

        visitedSet.add(0)
        bfs_queue.append(0)

        while bfs_queue:
            node = bfs_queue.popleft()
            for nei in neighbors[node]:
                if nei not in visitedSet:
                    visitedSet.add(nei)
                    bfs_queue.append(nei)
                    if (nei, node) not in edges:
                        changed += 1
        return changed
        
        


        