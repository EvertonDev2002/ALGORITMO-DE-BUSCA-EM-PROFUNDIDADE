from depth_first_search import DepthFirstSearch
from graph import DirectedGraph

graph = DirectedGraph("G3.txt")
graph.load_graph()
algorithm = DepthFirstSearch(
    graph.list_vertices,
    graph.edges,
    graph.adjacent_list
    )
print(graph.adjacent_list)
print()
algorithm.dfs()
print('\n A chave do dicionário representa o vértice do grafo \n')
print(f'd: {algorithm.discovery}')
print(f'f: {algorithm.finish}')
