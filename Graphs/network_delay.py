from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Create Graph from edges
        graph = {i: [] for i in range(1, n+1)}
        for u,v,w in times:
            graph[u].append((v,w))

        minHeap = [(0,k)]
        heapq.heapify(minHeap) # pass something iterable to create heap
        visitedSet = set()
        answer = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            
            if node in visitedSet:
                continue
            
            visitedSet.add(node)
            answer = max(answer, time)

            for nei, travel in graph[node]:
                if nei not in visitedSet:
                    heapq.heappush(minHeap, (time+travel, nei))
        
        if len(visitedSet) == n:
            return answer
        else:
            return -1
        # TC : O(E log V)


       


        