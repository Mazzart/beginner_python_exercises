"""Depth-first search (DFS)
Algorithm for traversing or searching tree or graph data structures.
"""

GRAPH_EXAMPLE = {'A': {'B', 'C'},
                 'B': {'A', 'D', 'E'},
                 'C': {'A', 'F'},
                 'D': {'B'},
                 'E': {'B', 'F'},
                 'F': {'C', 'E'}}


def depth_first_search(graph: dict, start: str) -> set:
    """Return possible vertices down each branch"""

    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


print(depth_first_search(GRAPH_EXAMPLE, 'A'))
