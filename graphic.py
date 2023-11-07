from typing import Dict, Tuple


class Graphic:
    def __init__(self, edges_label: Dict[Tuple[int, int], str]) -> None:
        self.edges_label = edges_label
