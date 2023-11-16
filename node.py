"""
This file contains the Node class, which is used to represent a node in the grid.
"""
from typing import Callable, Optional


class Node:
    """
    This class represents a node in the grid.

    Attributes:
        pos: the (x, y) coordinates of the node
        parent: the (x, y) coordinates of the parent node
        start_distance: the distance from the start node
        goal_distance: the distance from the goal node
        diagonal_neighbors: whether diagonal neighbors are allowed

    Methods:
        get_neighbors: returns a list of the neighbors of the node
    """

    def __init__(self, pos: tuple[int, int], destination: tuple[int, int],
                 heuristic_function: Callable[[tuple[int, int], tuple[int, int]], int],
                 parent: Optional['Node'] = None, start_distance: int = 0,
                 diagonal_neighbors: bool = False):
        """
        :param pos: the (x, y) coordinates of the node
        :param destination: the (x, y) coordinates of the destination node
        :param heuristic_function: the heuristic function to use
        :param parent: the parent node
        :param start_distance: the distance from the start node
        :param diagonal_neighbors: whether diagonal neighbors are allowed
        """
        # Node's Positions
        self.pos = pos
        self.destination = destination
        self.parent = parent

        # Distances
        self.heuristic_function = heuristic_function
        self.start_distance = start_distance
        self.goal_distance = heuristic_function(pos, destination)
        self.diagonal_neighbors = diagonal_neighbors

    def __str__(self) -> str:
        """
        return: a string representation of the node
        """
        return f"Node: {self.pos}"

    def __eq__(self, other: object) -> bool:
        """
        return: whether the two nodes are equal
        """
        if not isinstance(other, Node):
            return False
        return self.pos == other.pos

    def get_neighbor_node(self, update: tuple[int, int]) -> 'Node':
        """
        Returns: the neighbor node
        """
        return Node((self.pos[0] + update[0], self.pos[1] + update[1]), self.destination,
                    self.heuristic_function, self, self.start_distance + 1, self.diagonal_neighbors)

    def get_coordinates(self) -> tuple[int, int]:
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
            return [self.get_neighbor_node((0, 1)), self.get_neighbor_node((1, 0)),
                    self.get_neighbor_node((0, -1)), self.get_neighbor_node((-1, 0)),
                    self.get_neighbor_node((1, 1)), self.get_neighbor_node((1, -1)),
                    self.get_neighbor_node((-1, 1)), self.get_neighbor_node((-1, -1))]

        # Otherwise, return only the 4 cardinal neighbors
        return [self.get_neighbor_node((0, 1)), self.get_neighbor_node((1, 0)),
                self.get_neighbor_node((0, -1)), self.get_neighbor_node((-1, 0))]
