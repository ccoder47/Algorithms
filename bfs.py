from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search traversal from start node.
    graph: dict of node→list of neighbors.
    Returns list of visited nodes.
    """
    visited, queue = set(), deque([start])
    order = []
    visited.add(start)
    while queue:
        node = queue.popleft()
        order.append(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return order

if __name__ == "__main__":
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': ['F'], 'F': []
    }
    print("BFS order:", bfs(sample_graph, 'A'))
