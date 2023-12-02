#used for finding the shortest path in weighted graphs.
import heapq

# Graph representation using dictionaries
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5, 'E': 2},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        # Skip if already found a shorter path
        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print(distances)

# Dijkstra's algorithm example usage
print("Dijkstra's algorithm:")
dijkstra(graph, 'A')
