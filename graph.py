from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flow_solver import FlowSolver

class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.arcs: list[Arc] = []

class Arc:
    def __init__(self, start_node: Node, end_node: Node, capacity: int) -> None:
        self.start_node = start_node
        self.end_node = end_node
        self.capacity = capacity
        self.flow = 0
        self.reverse: 'Arc' = None

    def resiudal_capacity(self) -> int:
        return self.capacity - self.flow
    
    def set_reverse_arc(self) -> None:
        self.reverse = Arc(self.end_node, self.start_node, 0)
        self.end_node.arcs.append(self.reverse) 

class Graph:
    def __init__(self) -> None:
        self.nodes_by_name: dict[str, Node] = {}
        self.arcs: list[Arc] = []

    def __add_node(self, node_name: str) -> Node:
        node = Node(node_name)
        self.nodes_by_name[node_name] = node
        return node

    def add_arc(self, start_name: str, end_name: str, capacity: int) -> None:
        if start_name not in self.nodes_by_name:
            self.__add_node(start_name)
        if end_name not in self.nodes_by_name:
            self.__add_node(end_name)
        start_node = self.nodes_by_name[start_name]
        end_node = self.nodes_by_name[end_name]
        arc = Arc(start_node, end_node, capacity)
        arc.set_reverse_arc()
        self.arcs.append(arc)
        start_node.arcs.append(arc)
    
    def solve_flow(self, solver: 'FlowSolver', source: Node, sink: Node) -> int:
        return solver.solve(source, sink)