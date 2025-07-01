def dfs(graph, start, visited=None, order=None):
    """
    Depth-First Search traversal (recursive).
    Returns list of visited nodes.
    """
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for nbr in graph.get(start, []):
        if nbr not in visited:
            dfs(graph, nbr, visited, order)
    return order

if __name__ == "__main__":
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': ['F'], 'F': []
    }
    print("DFS order:", dfs(sample_graph, 'A'))
