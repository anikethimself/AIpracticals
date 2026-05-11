from collections import deque

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main Function
def main():
    graph = {}

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node = input(f"\nEnter node {i+1}: ")
        
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        
        graph[node] = neighbors

    start = input("\nEnter starting node: ")

    print("\nDFS Traversal:")
    visited = set()
    dfs(graph, start, visited)

    print("\n\nBFS Traversal:")
    bfs(graph, start)

if __name__ == "__main__":
    main()
