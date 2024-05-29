from graph import Graph
from flow_solver import EdmondKarp

if __name__ == "__main__":
    graph = Graph()
    graph.add_arc('s', 'a', 20)
    graph.add_arc('s', 'b', 10)
    graph.add_arc('a', 'c', 10)
    graph.add_arc('b', 'c', 10)
    graph.add_arc('a', 'd', 5)
    graph.add_arc('c', 'd', 5)
    graph.add_arc('c', 't', 10)
    graph.add_arc('d', 't', 15)

    max_flow = EdmondKarp().solve(graph.nodes_by_name['s'], graph.nodes_by_name['t'])
    print(f'Maximum flow: {max_flow}')