from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS in undirected graph 
        pacific, atlantic = set(), set()
        m, n = len(heights), len(heights[0])
        answer = []

        def dfs(row, col, visit, prevHeight):
            if (row, col) in visit or row < 0 or col < 0 or row == m or col == n or heights[row][col] < prevHeight:
                return
            visit.add((row,col))
            dfs(row+1, col, visit, heights[row][col])
            dfs(row-1, col, visit, heights[row][col])
            dfs(row, col+1, visit, heights[row][col])
            dfs(row, col-1, visit, heights[row][col])
        
        for col in range(n):
            dfs(0, col, pacific, 0)
            dfs(m-1, col, atlantic, 0)
        
        for row in range(m):
            dfs(row, 0, pacific, 0)
            dfs(row, n-1, atlantic, 0)
        
        for row in range(m):
            for col in range(n):
                if (row,col) in pacific and (row,col) in atlantic:
                    answer.append([row,col])
        return answer



        