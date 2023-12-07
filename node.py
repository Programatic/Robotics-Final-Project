"""
This file contains the Node class, which is used to represent a node in the grid.
"""
from functools import total_ordering
from typing import Any, Callable, Optional, TypeAlias

import numpy as np

Position: TypeAlias = tuple[int, int]
HeuristicFunction: TypeAlias = Callable[[Position, Position], int]


# Used to generate other comparisons from __eq__ and __lt__
@total_ordering
class Node:
    """Node Class"""
    worldmap_reference: np.ndarray['Node', Any]
    end_coordinate: Position
    diagonal_neighbors: bool = False
    cost_addition: int = 1

    def __init__(self, pos: Position, is_obstacle: bool, heuristic_distance: float):
        """
        :param pos: the (x, y) coordinates of the node
        :param destination: the (x, y) coordinates of the destination node
        :param heuristic_function: the heuristic function to use
        :param diagonal_neighbors: whether diagonal neighbors are allowed
        """
        self.pos = pos
        self.is_obstacle = is_obstacle
        self.heuristic_distance = heuristic_distance
        self.parent_node: Optional['Node'] = None
        self.cost = 0
        self.is_explored = False

    def __str__(self) -> str:
        """
        return: a string representation of the node
        """
        return f"Node: {self.pos}"

    def __eq__(self, other: object) -> bool:
        """
        return: whether the two nodes are equal or whether the node has the same coordinates as the tuple
        """
        if isinstance(other, tuple):
            return self.pos == other
        if not isinstance(other, Node):
            return False
        return self.pos == other.pos and self.heuristic_distance == other.heuristic_distance

    def __lt__(self, other: object) -> bool:
        """Implements less than for Nodes."""
        if isinstance(other, Node):
            return self.heuristic_distance < other.heuristic_distance
        raise NotImplementedError("Only supports comparison of Nodes.")

    def __hash__(self) -> int:
        """
        Node hash function.

        Returns
        -------
        int
            Hash code.
        """
        return hash(self.pos)

    def get_neighbor_node(self, update: Position) -> Optional['Node']:
        """
        Returns: the neighbor node
        """
        x = self.pos[0] + update[0]
        y = self.pos[1] + update[1]

        if x < 0 or y < 0:
            return None

        if x > len(self.worldmap_reference) - 1 or y > len(self.worldmap_reference[0]) - 1:
            return None

        neighbor = self.worldmap_reference[x, y]
        weight = 1
        if abs(update[0]) + abs(update[1]) > 1:
            weight = 2 ** 0.5

        neighbor.cost = self.cost_addition * weight + self.cost
        return neighbor
        # type: ignore

    def get_coordinates(self) -> Position:
        """
        return: the (x, y) coordinates of the node
        """
        return self.pos

    def get_neighbors(self) -> list['Node']:
        """
        return: a list of the neighbors of the node
        """
        # if diagonal neighbors are allowed, return all 8 neighbors
        if self.diagonal_neighbors:
            node_with_none_list = [self.get_neighbor_node((0, 1)), self.get_neighbor_node((1, 0)),
                                   self.get_neighbor_node((0, -1)), self.get_neighbor_node((-1, 0)),
                                   self.get_neighbor_node((1, 1)), self.get_neighbor_node((1, -1)),
                                   self.get_neighbor_node((-1, 1)), self.get_neighbor_node((-1, -1))]
        else:
            node_with_none_list = [self.get_neighbor_node((0, 1)), self.get_neighbor_node((1, 0)),
                                   self.get_neighbor_node((0, -1)), self.get_neighbor_node((-1, 0))]

        node_list: list[Node] = []

        for node_none in node_with_none_list:
            if node_none:

                if node_none.is_explored:
                    continue

                if not node_none.traversable():
                    continue

                node_none.parent_node = self
                node_none.is_explored = True
                node_none.heuristic_distance += node_none.cost
                node_list.append(node_none)

        return node_list

    def traversable(self) -> bool:
        """
        return: True if the node can be traversed, False otherwise
        """
        return not self.is_obstacle
