"""
This file contains the Node class, which is used to represent a node in the grid.
"""


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
    def __init__(self, x: int, y: int, parent_x: int, parent_y: int,
                 start_distance: float, goal_distance: float,
                 diagonal_neighbors: bool = False):
        """
        :param x: the x coordinate of the node
        :param y: the y coordinate of the node
        :param parent_x: the x coordinate of the parent node
        :param parent_y: the y coordinate of the parent node
        :param start_distance: the distance from the start node
        :param goal_distance: the distance from the goal node
        :param diagonal_neighbors: whether diagonal neighbors are allowed
        """
        self.pos = (x, y)
        self.parent = (parent_x, parent_y)
        self.start_distance = start_distance
        self.goal_distance = goal_distance
        self.diagonal_neighbors = diagonal_neighbors

    def __str__(self) -> str:
        """
        return: a string representation of the node
        """
        return f"Node: ({self.pos})"

    def get_neighbors(self) -> list[tuple[int, int]]:
        """
        return: a list of the neighbors of the node
        """
        # if diagonal neighbors are allowed, return all 8 neighbors
        if self.diagonal_neighbors:
            return [(self.pos[0], self.pos[1] + 1), (self.pos[0] + 1, self.pos[1]),
                    (self.pos[0], self.pos[1] - 1), (self.pos[0] - 1, self.pos[1]),
                    (self.pos[0] + 1, self.pos[1] + 1), (self.pos[0] + 1, self.pos[1] - 1),
                    (self.pos[0] - 1, self.pos[1] + 1), (self.pos[0] - 1, self.pos[1] - 1)]

        # Otherwise, return only the 4 cardinal neighbors
        return [(self.pos[0], self.pos[1] + 1), (self.pos[0] + 1, self.pos[1]),
                (self.pos[0], self.pos[1] - 1), (self.pos[0] - 1, self.pos[1])]
