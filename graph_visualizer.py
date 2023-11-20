from typing import Dict, Tuple, List
from matplotlib.pyplot import axis, show, legend
from matplotlib.lines import Line2D
from networkx import \
    draw_networkx_nodes, \
    draw_networkx_labels, \
    draw_networkx_edges, \
    DiGraph, \
    shell_layout  # type: ignore


class GraphVisualizer:
    def __init__(
        self,
        edges_label: Dict[Tuple[int, int], str],
        finish: Dict[int, int],
        discovery: Dict[int, int],
        vertices: List[int]
    ) -> None:
        self.__edges_label: Dict[Tuple[int, int], str] = edges_label
        self.__discovery: Dict[int, int] = discovery
        self.__finish: Dict[int, int] = finish
        self.__di_graph: DiGraph = DiGraph()
        self.__vertices: List[int] = vertices
        self.__times: Dict[int, Tuple[int, int]] = {}
        self.__node_label: Dict[int, str] = {}
        self.__edge_colors_list: List[str] = []
        self.__nomenclature_colors: Dict[str, str] = {
            'árvore': 'blue',
            'retorno': 'green',
            'avanço': 'orange',
            'cruzamento':  'red'
        }

    def __add_vertices(self) -> None:
        self.__di_graph.add_nodes_from(self.__vertices)

    def __add_edge(self) -> None:

        for vertex, adjacent in list(self.__edges_label.keys()):

            nomenclature = self.__edges_label[(vertex, adjacent)]

            match nomenclature:
                case 'árvore':
                    self.__di_graph.add_edge(
                        vertex,
                        adjacent,
                        label=nomenclature,
                    )
                case 'retorno':
                    self.__di_graph.add_edge(
                        vertex,
                        adjacent,
                        label=nomenclature,
                    )
                case 'avanço':
                    self.__di_graph.add_edge(
                        vertex,
                        adjacent,
                        label=nomenclature,
                    )
                case 'cruzamento':
                    self.__di_graph.add_edge(
                        vertex,
                        adjacent,
                        label=nomenclature,
                    )
                case _:
                    print("Sem nomenclatura")

    def __edge_colors(self) -> None:

        self.__edge_colors_list = [
            self.__nomenclature_colors[self.__edges_label[edge]]
            for edge in self.__di_graph.edges()
        ]

    def __add_time(self) -> None:
        for vertex in self.__vertices:
            self.__times.setdefault(
                vertex,
                (
                    self.__discovery[vertex],
                    self.__finish[vertex]
                )
            )

    def __add_node_labels(self) -> None:
        if not self.__times:
            self.__add_time()

        self.__node_label = {
            vertex: f"{vertex}\n({d}/{f})"
            for vertex, (d, f) in self.__times.items()
        }

    def draw(self) -> None:
        if not self.__node_label:  # Ordem importa
            self.__add_vertices()
            self.__add_edge()
            self.__edge_colors()
            self.__add_node_labels()

        draw_networkx_nodes(
            self.__di_graph,
            shell_layout(self.__di_graph),
            node_size=3000,
            node_color="black",
        )
        draw_networkx_labels(
            self.__di_graph,
            shell_layout(self.__di_graph),
            labels=self.__node_label,
            font_color='white',
            font_weight='bold',
            font_size=10
        )
        draw_networkx_edges(
            self.__di_graph,
            shell_layout(self.__di_graph),
            arrowsize=10,
            arrows=True,
            min_target_margin=29,
            connectionstyle="arc3,rad=0.1",
            edge_color=self.__edge_colors_list  # noqa: E261 # type: ignore
            )
        # draw_networkx_edge_labels(
        #     self.__di_graph,
        #     shell_layout(self.__di_graph),
        #     edge_labels=self.__edges_label,
        #     font_size=12,
        # )

        handles = [
            Line2D(
                [0],
                [0],
                marker='o',
                color='w',
                markerfacecolor=color,
                markersize=10,
                label=label
            )
            for label, color in self.__nomenclature_colors.items()
        ]

        legend(handles=handles, loc='upper left')
        axis('off')
        show()
