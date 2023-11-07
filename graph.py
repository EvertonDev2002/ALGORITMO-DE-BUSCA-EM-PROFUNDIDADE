from typing import Dict, List, Tuple


class DirectedGraph:
    def __init__(self, text_file: str) -> None:
        self.__adjacent_list: Dict[int, List[int]] = {}
        self.__edges: Dict[Tuple[int, int], str] = {}
        self.__number_edges: int = 0
        self.__verteces: List[int] = []
        self.__number_vertices: int = 0
        self.text_file = text_file

    def load_graph(self) -> None:
        with open(self.text_file, "r") as file:
            lines = file.readlines()

            self.__verteces: List[int] = [
                (vertex + 1)
                for vertex in range(
                    int(
                        lines[:1][0][:2]
                        )
                    )
                ]

            for line in lines[1:]:

                vertex, adjacent = map(
                    lambda value: int(value),
                    line.split()
                )

                self.__adjacent_list.setdefault(
                    vertex, []
                    ).append(adjacent)

                self.__edges.setdefault(
                    (vertex, adjacent), ''
                    )

            for vertex in set(self.__verteces):
                if vertex not in list(self.adjacent_list.keys()):
                    self.__adjacent_list.setdefault(
                        vertex,
                        []
                    )

            self.__verteces = list(self.adjacent_list.keys())

    @property
    def adjacent_list(self) -> Dict[int, List[int]]:
        self.__adjacent_list = dict(
            sorted(
                self.__adjacent_list.items(),
                key=lambda item: len(item[1]),
                reverse=True
                )
            )

        return self.__adjacent_list

    @property
    def list_vertices(self) -> List[int]:
        return self.__verteces

    @property
    def number_vertices(self) -> int:
        if not self.__number_vertices:
            self.__length_vertices()
        return self.__number_vertices

    def __length_vertices(self) -> None:
        self.__number_vertices = len(
            self.__verteces
            )

    @property
    def edges(self) -> Dict[Tuple[int, int], str]:
        return self.__edges

    @property
    def number_edges(self) -> int:
        if not self.__number_edges:
            self.__length_edges()
        return self.__number_edges

    def __length_edges(self) -> None:
        self.__number_edges = len(
            self.__edges
        )
