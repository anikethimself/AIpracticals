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

def main():
    graph ={}

    n= int(input("Enter the no. of nodes:"))

    for i in range(n):
        node = input(f"\nEnter the node {i+1}:")
        neighbor = input(f"Enter the neighbor nodes of {node} node:").split()
        graph[node] = neighbor

    start = input("\nEnter the start node:")

    print("\n DFS Traversal:")
    visited = set()
    dfs(graph, start, visited)

    print("\n BFS Traversal:")
    bfs(graph, start)

if __name__ == "__main__":
        main()
