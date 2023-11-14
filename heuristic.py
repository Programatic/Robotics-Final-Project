"""
This script contains heuristic functions that is used for determining the best
path to traverse in the maze.
"""
import random
from node import Node


def manhattan_distance(node1: Node, node2: Node) -> float:
    """
    Calculates the Manhattan distance between two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: the Manhattan distance between the two nodes
    """
    return abs(node1.pos[0] - node2.pos[0]) + abs(node1.pos[1] - node2.pos[1])


def bozo_distance() -> float:
    """
    Calculates the Bozo distance between two nodes.

    :return: the Bozo distance between the two nodes
    """
    return random.randint(0, 100)
