"""
This file contains the Node class, which is used to represent a node in the grid.
"""
class Node:
    def __init__(self, x, y, parent_x, parent_y, start_distance, goal_distance, diagonal_neighbors=False):
        """
        :param x: the x coordinate of the node
        :param y: the y coordinate of the node
        :param parent_x: the x coordinate of the parent node
        :param parent_y: the y coordinate of the parent node
        :param start_distance: the distance from the start node
        :param goal_distance: the distance from the goal node
        :param diagonal_neighbors: whether diagonal neighbors are allowed
        """
        self.x = x
        self.y = y
        self.parent_x = parent_x
        self.parent_y = parent_y
        self.start_distance = start_distance
        self.goal_distance = goal_distance
        self.diagonal_neighbors = diagonal_neighbors


    def __str__(self):
        """
        return: a string representation of the node
        """
        return "Node: (" + str(self.x) + ", " + str(self.y) + ")"

    def get_neighbors(self):
        """
        return: a list of the neighbors of the node
        """
        if self.diagonal_neighbors:
            return [[x, y + 1], [x + 1, y], [x, y - 1], [x - 1, y], [x + 1, y + 1],
                    [x + 1, y - 1], [x - 1, y + 1], [x - 1, y - 1]]
        else:
            return [[x, y + 1], [x + 1, y], [x, y - 1], [x - 1, y]]
