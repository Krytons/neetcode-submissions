class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return - 1

        directions = [(-1, -1), (-1,0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0,0))
        length = 1

        maxRow = len(grid) - 1  
        maxColumn = len(grid[0]) -1 

        while queue:
            print(f"New queue read");
            runs = len(queue)
            for index in range(runs):
                cr, cc = queue.popleft()
                print(f"Reading {cr},{cc}");
                if cr == maxRow and cc == maxColumn:
                    return length
                
                for dr, dc in directions:
                    nr = dr + cr
                    nc = dc + cc
                    print(f"Evaluating {nr},{nc}");
                    if min(nr, nc) < 0 or nr > maxRow or nc > maxColumn or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    print(f"Pushing {nr},{nc}"); 
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            
            length += 1

        
        return -1