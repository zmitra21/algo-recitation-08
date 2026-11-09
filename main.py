# Zack Mitra

from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        node = frontier.pop()
        for neighbor in graph[node]:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)        
    return result

def connected(graph):
    if len(graph) == 0:
        return True

    start_node = next(iter(graph))
    reachable_nodes = reachable(graph, start_node)

    return len(reachable_nodes) == len(graph)

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            component = reachable(graph, node)
            visited.update(component)
            count += 1

    return count

