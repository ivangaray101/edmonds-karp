from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph import Node, Arc

class FlowSolver(ABC):
    @abstractmethod
    def solve(self, source: 'Node', sink: 'Node') -> int:
        return

class EdmondKarp(FlowSolver):
    def __bfs(self, source: 'Node', sink: 'Node') -> list['Arc']:
        visited = set()
        queue = [source]
        visited.add(source)
        parent: dict['Node', 'Arc'] = {}

        while queue:
            current_node: 'Node' = queue.pop()
            for arc in current_node.arcs:
                if arc.end_node not in visited and arc.resiudal_capacity() > 0:
                    queue.append(arc.end_node)
                    visited.add(arc.end_node)
                    parent[arc.end_node.name] = arc

                    if arc.end_node == sink:
                        path = []
                        v = sink.name
                        while v != source.name:
                            path.append(parent[v])
                            arc = parent[v]
                            v = arc.start_node.name
                        path.reverse()
                        return path
        return None

    def solve(self, source: 'Node', sink: 'Node') -> int:
        max_flow: int = 0
        while True:
            path = self.__bfs(source, sink)

            if not path:
                break

            path_flow = float('Inf')
            for arc in path:
                path_flow = min(path_flow, arc.resiudal_capacity())
            
            for arc in path:
                arc.flow += path_flow
                arc.reverse.flow -= path_flow
            
            max_flow += path_flow
            
        return max_flow
