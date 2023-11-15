from typing import Dict, List, Tuple


class DepthFirstSearch:
    def __init__(
        self,
        vertices: List[int],
        edges_label: Dict[Tuple[int, int], str],
        adjacent_list: Dict[int, List[int]]
    ) -> None:
        self.vertices = vertices
        self.adjacent_list = adjacent_list
        self.color: Dict[int, str] = {
            key: 'Branco'
            for key in vertices
        }
        self.discovery: Dict[int, int] = {
            key: 0
            for key in vertices
        }
        self.finish: Dict[int, int] = {
            key: 0
            for key in vertices
        }
        self.mark = 0
        self.edges_label = edges_label

    def dfs(self):
        for vertex in self.vertices:
            if self.color[vertex] == 'Branco':
                self.dfs_visit(vertex)

    def dfs_visit(self, vertex: int):
        self.color[vertex] = 'Cinza'
        self.mark += 1
        self.discovery[vertex] = self.mark

        for adjacent in self.adjacent_list[vertex]:
            if self.color[adjacent] == 'Branco':

                print(f'{vertex, adjacent}: árvore')
                self.edges_label[(vertex, adjacent)] = 'árvore'

                self.dfs_visit(adjacent)

            elif self.color[adjacent] == 'Cinza':

                print(f'{vertex, adjacent}: retorno')
                self.edges_label[(vertex, adjacent)] = 'retorno'

            elif self.discovery[vertex] < self.discovery[adjacent]:

                print(f'{vertex, adjacent}: avanço')
                self.edges_label[(vertex, adjacent)] = 'avanço'
            else:
                print(f'{vertex, adjacent}: cruzamento')
                self.edges_label[(vertex, adjacent)] = 'cruzamento'

        self.color[vertex] = 'Preto'
        self.mark += 1
        self.finish[vertex] = self.mark
