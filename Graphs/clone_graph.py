class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        
        ## Points to be noted
        # Connected Undirected graph
        # whole graph can be visited using DFS or BFS
        

        # DFS appraoch
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(val = node.val)
            oldToNew[node] = copy # Similar to visited set

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)
        
        # BFS approach
        """
        traverse_queue = deque([node])
        copy = Node(node.val)
        oldToNew[node] = copy

        while traverse_queue:
            curr = traverse_queue.popleft()

            for nei in curr.neighbors:
                if nei not in oldToNew:
                    traverse_queue.append(nei)
                    oldToNew[nei] = Node(nei.val)
                
                oldToNew[curr].neighbors.append(oldToNew[nei])
        return oldToNew[node]
        """

        # TC: O(N + E) N is number of nodes and E is number of edges
        # SC: O(N) for hashmap and O(N) for recursion stack in worst case



        