"""Dijkstra algorithm

Finds the shortest path from one vertex of the graph to all other vertices
"""

GRAPH = {'start': {'A': 6, 'B': 2}, 'A': {'finish': 1}, 'B': {'A': 3, 'finish': 5}, 'finish': {}}

INFINITY = float("inf")
costs = {'A': 6, 'B': 2, 'finish': INFINITY}
parents = {'A': 'start', 'B': 'start', 'finish': None}
processed = []


def find_lowest_cost_node(costs):
    """Return the lowest cost of the node"""

    lowest_cost = float("inf")
    lowest_cost_node = None

    # go through all the nodes
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost  # the new node with lowest cost
            lowest_cost_node = node
    return lowest_cost_node


# the node with the lowest cost among the processed
node = find_lowest_cost_node(costs)

while node is not None:  # if all nodes are processed end while cycle
    cost = costs[node]
    neighbors = GRAPH[node]
    # go through all the neighbors of the node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # if you reach your neighbor faster on the current node
        if costs[n] > new_cost:
            # update node cost
            costs[n] = new_cost
            # this node becomes the new parent for the neighbor
            parents[n] = node

    processed.append(node)  # the node is marked as processed

    node = find_lowest_cost_node(costs)

print(f"The fastest way has a cost of {new_cost}.")
