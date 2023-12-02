'''
BFS is an algorithm used to traverse
or search a graph or tree data structure
unwighted.
'''

from collections import deque

# Graph representation using dictionaries
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex])

# BFS example usage
print("BFS:")
bfs(graph, 'A')
