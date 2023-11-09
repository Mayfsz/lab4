from typing import Tuple, Union, Iterable

Node = Union[str, int]
Edge = Tuple[Node, Node]


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        self.directed = directed
        self.graph = {}
        for edge in edges:
            self.add_edge(edge)

    def has_node(self, node: Node):
        """Whether a node is in graph"""
        return node in self.graph

    def has_edge(self, edge: Edge):
        """Whether an edge is in the graph"""
        node1, node2 = edge
        if self.has_node(node1) and self.has_node(node2):
            return node2 in self.graph[node1]
        return False

    def add_node(self, node: Node):
        """Add a node"""
        if not self.has_node(node):
            self.graph[node] = set()

    def add_edge(self, edge: Edge):
        """Add an edge (node1, node2). For directed graph, node1 -> node2"""
        node1, node2 = edge
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)

    def remove_node(self, node: Node):
        """Remove a node and all its references"""
        if node in self.graph:
            del self.graph[node]
            for other_node in self.graph:
                self.graph[other_node] = {
                    n for n in self.graph[other_node] if n != node
                }
        else:
            raise ValueError(f"Node {node} not found in the graph")

    def remove_edge(self, edge: Edge):
        """Remove an edge from the graph"""
        if self.has_edge(edge):
            node1, node2 = edge
            self.graph[node1].remove(node2)
            if not self.directed:
                self.graph[node2].remove(node1)
        else:
            raise ValueError(f"The edge {edge} does not exist in the graph.")

    def indegree(self, node: Node) -> int:
        """Compute indegree for a node"""
        if node not in self.graph:
            raise ValueError(f"Node '{node}' is not in the graph")
        if node in self.graph:
            indegree_count = 0
            for other_node in self.graph:
                if node in self.graph[other_node]:
                    indegree_count += 1
            return indegree_count
        return 0

    def outdegree(self, node: Node) -> int:
        """Compute outdegree for a node"""
        if node in self.graph:
            return len(self.graph[node])
        return 0

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return repr(self.graph)
