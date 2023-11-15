"""
This script contains heuristic functions that is used for determining the best
path to traverse in the maze.
"""
import random
from node import Node


def manhattan_distance(node1: tuple[int, int], node2: tuple[int, int]) -> int:
    """
    Calculates the Manhattan distance between two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: the Manhattan distance between the two nodes
    """
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def bozo_distance() -> int:
    """
    Calculates the Bozo distance between two nodes.

    :return: the Bozo distance between the two nodes
    """
    return random.randint(0, 100)
