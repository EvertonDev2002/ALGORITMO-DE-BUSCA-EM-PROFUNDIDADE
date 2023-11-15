from depth_first_search import DepthFirstSearch
from graph import DirectedGraph
from GraphVisualizer import GraphVisualizer

graph = DirectedGraph("G.txt")  # <- Arquivo do grafo
graph.load_graph()

algorithm = DepthFirstSearch(
    graph.list_vertices,
    graph.edges,
    graph.adjacent_list
)
algorithm.dfs()

plot = GraphVisualizer(
    algorithm.edges_label,
    algorithm.finish,
    algorithm.discovery,
    graph.list_vertices
)

print('\n A chave do dicionário representa o vértice do grafo \n')
print(f'd: {algorithm.discovery}')
print(f'f: {algorithm.finish}')
print(f'\n Lista de adjacência: {graph.adjacent_list}\n')

plot.draw()
