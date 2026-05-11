from collections import deque

# DFS Function
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main Function
def main():
    graph = {}

    # Number of nodes
    n = int(input("Enter number of nodes: "))

    # Taking graph input
    for i in range(n):
        node = input(f"\nEnter node {i+1}: ")
        
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        
        graph[node] = neighbors

    # Starting node
    start = input("\nEnter starting node: ")

    # DFS Traversal
    print("\nDFS Traversal:")
    visited = set()
    dfs(graph, start, visited)

    # BFS Traversal
    print("\n\nBFS Traversal:")
    bfs(graph, start)

# Driver Code
if __name__ == "__main__":
    main()