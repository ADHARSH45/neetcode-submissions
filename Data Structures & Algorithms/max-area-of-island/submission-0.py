class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row , col = len(grid),len(grid[0])
        area = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]


        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1

            while q:
                ro,cl = q.popleft()
                for dr,dc in directions:
                    nr,nc = ro+dr,cl+dc
                    if nr<0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] == 0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    res += 1
            
            return res

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = max(area,bfs(r,c))

        return area


        