import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    open_list = []
    count = 0
    heapq.heappush(open_list, (0, count, start))
    
    came_from = {}
    g_cost = {start: 0}
    
    while open_list:
        _, _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        x, y = current
        
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1
                
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), goal)
                    count += 1
                    heapq.heappush(open_list, (f_cost, count, (nx, ny)))
                    came_from[(nx, ny)] = current
    
    return None


# INPUT
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter grid (0 = path, 1 = obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input().split()))
    if len(row) != cols:
        print("Invalid row length!")
        exit()
    grid.append(row)

print("Enter start position (row col):")
start = tuple(map(int, input().split()))

print("Enter goal position (row col):")
goal = tuple(map(int, input().split()))

# VALIDATION
if not (0 <= start[0] < rows and 0 <= start[1] < cols):
    print("Invalid start position!")
    exit()

if not (0 <= goal[0] < rows and 0 <= goal[1] < cols):
    print("Invalid goal position!")
    exit()

if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
    print("Start or Goal is on obstacle!")
    exit()

path = astar(grid, start, goal)

if path:
    print("Path found:")
    for p in path:
        print(p, end=" ")
else:
    print("No path found")