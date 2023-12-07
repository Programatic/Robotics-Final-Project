"""
This file contains the search algorithms that are used to find the path from the start node to the end node
"""
from queue import PriorityQueue

from node import Node, Position
import utils as util


def a_star(start: Position, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the priority queue, the explored set, and the depth
    queue, depth = util.initialize_algorithm(start)

    # While the queue is not empty and the depth limit is not reached
    while not queue.empty() and depth < depth_limit:
        # Update the depth
        depth += 1

        # Get the current node and add it to the explored set
        current_node = queue.get()

        # If the current node is the goal node
        if current_node == Node.end_coordinate:
            return util.backtrack(current_node, start)

        # Add the neighbors that can be explored to the queue
        for neighbor in current_node.get_neighbors():
            queue.put(neighbor)

    # Return an empty list if the path is not found
    print(depth)
    return []


def beam(start: Position, k: int = 50, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param k: the number of nodes to keep in the frontier
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the frontier set and the depth
    queue, depth = util.initialize_algorithm(start)
    depth = 0

    frontier: list[Node] = [queue.get()]

    # While the frontier is not empty
    while frontier and depth < depth_limit:
        # Update the depth
        depth += 1
        queue = PriorityQueue()

        # Add the neighbors to the frontier
        for node in frontier:
            # If the current node is the goal node
            if node == Node.end_coordinate:
                return util.backtrack(node, start)

        for node in frontier:
            for neighbor in node.get_neighbors():
                queue.put(neighbor)

        frontier = []

        for _ in range(k):
            frontier.append(queue.get())

    # Return an empty list if the path is not found
    print(depth)
    return []


# def brushfire(start: Position, depth_limit: int = 50) -> list[Position]:
#     """
#     :param heuristic: the heuristic function to use for calculating the distance between two nodes
#     :param diagonal_neighbors: whether diagonal neighbors are allowed
#     :param depth_limit: the depth limit of the search
#     Returns: a list of nodes that represents the path from the start node to the end node
#     """
#     # TO DO: Implement this function
#     return []
