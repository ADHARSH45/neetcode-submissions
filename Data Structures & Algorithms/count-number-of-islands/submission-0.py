class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        row = len(grid)
        col = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            

            while q:
                ro,cl = q.popleft()
                for dr,dc in directions:
                    nr,nc = ro+dr,cl+dc
                    if(nr < 0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] == "0"): 
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands


        