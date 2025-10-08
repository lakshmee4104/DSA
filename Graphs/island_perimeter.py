from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    edges = 0
                    if i+1 < rows and grid[i+1][j] == 1:
                        edges += 1
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        edges += 1
                    if j+1 < cols and grid[i][j+1] == 1:
                        edges += 1
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        edges += 1
                    perimeter += 4-(edges)
        return perimeter


        