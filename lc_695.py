class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        self.max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.island_area = 0
                    self.infect(grid, i, j)
        return self.max_area
    
    def infect(self, grid, i, j):
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 1:
            return
        self.island_area += 1
        self.max_area = max(self.max_area, self.island_area)
        grid[i][j] = -1
        self.infect(grid, i+1, j)
        self.infect(grid, i-1, j)
        self.infect(grid, i, j+1)
        self.infect(grid, i, j-1)

sol = Solution()
grid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(sol.maxAreaOfIsland(grid))
