"""
This script contains heuristic functions that is used for determining the best
path to traverse in the maze.
"""
import random
from node import Position


def manhattan_distance(node1: Position, node2: Position) -> int:
    """
    Calculates the Manhattan distance between two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: the Manhattan distance between the two nodes
    """
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def euclidean_distance(node1: Position, node2: Position) -> int:
    """
    Calculates the Euclidean distance between two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: the Euclidean distance between the two nodes
    """
    return int(((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2) ** 0.5)


def chebyshev_distance(node1: Position, node2: Position) -> int:
    """
    Calculates the Chebyshev distance between two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: the Chebyshev distance between the two nodes
    """
    return max(abs(node1[0] - node2[0]), abs(node1[1] - node2[1]))


def octile_distance(node1: Position, node2: Position) -> int:
    """
    Calculates the Octile distance between two nodes.

    :param node1: node 1
    :param node2: node 2
    :return: the Octile distance between the two nodes
    """
    dx = abs(node1[0] - node2[0])
    dy = abs(node1[1] - node2[1])
    return int(dx + dy + (2 ** 0.5 - 2) * min(dx, dy))


def no_heuristic(_: Position, __: Position) -> int:
    """
    Returns 0 for no no_heuristic.
    """
    return 0


def bozo_distance(_: Position, __: Position) -> int:
    """
    Calculates the Bozo distance between two nodes.

    :return: the Bozo distance between the two nodes
    """
    return random.randint(0, 100)
