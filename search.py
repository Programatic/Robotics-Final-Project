"""
This file contains the search algorithms that are used to find the path from the start node to the end node
"""

from typing import Callable, Optional
from node import Node, Pos

# Tuples of (x, y) coordinates of the maze's start and end
start_coordinates: tuple[int, int] = (0, 0)
end_coordinates: tuple[int, int] = (100, 100)


'''
def a_star(heuristic: Callable[[tuple[int, int], tuple[int, int]], int],
           diagonal_neighbors: bool = False, depth_limit: int = 50) -> list[tuple[int, int]]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # TODO: Implement this function
    return []
'''


def greedy_first(heuristic: Callable[[tuple[int, int], tuple[int, int]], int],
                 diagonal_neighbors: bool = False, depth_limit: int = 50) -> list[tuple[int, int]]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the start node
    start = initialize_algorithm(heuristic, diagonal_neighbors)

    # Initialize the frontier
    frontier = [start]

    # Initialize the explored set
    explored = set()

    # Initialize the depth
    depth = 0

    # While the frontier is not empty
    while frontier and depth < depth_limit:
        # Update the depth
        depth += 1

        # Get the current node
        current_node = frontier.pop(0)
        explored.add(current_node)

        # If the current node is the goal node
        if current_node == end_coordinates:
            return backtrack(current_node)

        # Get the neighbors of the current node that can be explored
        neighbors = current_node.get_neighbors()
        neighbors[:] = [neighbor for neighbor in neighbors if neighbor not in explored]
        neighbors[:] = [neighbor for neighbor in neighbors if neighbor.traversable()]

        # Sort the neighbors by their heuristic value
        neighbors.sort(key=lambda neighbor: neighbor.goal_distance)

        # Add the neighbors to the frontier
        frontier.extend(neighbors)

    # Return an empty list if the path is not found
    return []


'''
def beam(heuristic: Callable[[tuple[int, int], tuple[int, int]], int], k: int = 2,
         diagonal_neighbors: bool = False, depth_limit: int = 50) -> list[tuple[int, int]]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # TODO: Implement this function
    return []


def brushfire(heuristic: Callable[[tuple[int, int], tuple[int, int]], int],
              diagonal_neighbors: bool = False, depth_limit: int = 50) -> list['Node']:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # TODO: Implement this function
    return []
'''


def initialize_algorithm(heuristic: Callable[[tuple[int, int], tuple[int, int]], int],
                         diagonal_neighbors: bool = False) -> Node:
    """
    This function is used to initialize anything that is needed for all of our algorithms to run.
    Returns:

    """
    return Node(pos=start_coordinates, destination=end_coordinates, heuristic_function=heuristic,
                diagonal_neighbors=diagonal_neighbors)


def backtrack(last_node: Optional[Node]) -> list[tuple[int, int]]:
    """
    This function is used to backtrack from the last node to the first node.
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    path = []
    current_node = last_node
    while current_node is not None:
        path.append(current_node.get_coordinates())
        current_node = current_node.parent
    return path[::-1]
