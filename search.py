"""
This file contains the search algorithms that are used to find the path from the start node to the end node
"""
from queue import PriorityQueue
from typing import TypeVar

from node import Node, Position


def a_star(start: Position, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the priority queue, the explored set, and the depth
    queue, explored, depth, back_path = initialize_algorithm(start)

    # While the queue is not empty and the depth limit is not reached
    while not queue.empty() and depth < depth_limit:
        # Update the depth
        depth += 1

        # Get the current node and add it to the explored set
        current_node = queue.get()
        back_path.append(current_node)

        # If the current node is the goal node
        if current_node == Node.end_coordinate:
            return backtrack(back_path)

        # Add the neighbors that can be explored to the queue
        for neighbor in neighbors(current_node, explored):
            explored.add(neighbor)
            queue.put(neighbor)

    # Return an empty list if the path is not found
    print(depth)
    return []


def beam(start: Position, k: int = 20, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param k: the number of nodes to keep in the frontier
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the frontier set and the depth
    queue, explored, depth, back_path = initialize_algorithm(start)
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
                return backtrack(back_path)

        for node in frontier:
            for neighbor in neighbors(node, explored):
                explored.add(neighbor)
                queue.put(neighbor)

        frontier = []

        for _ in range(k):
            frontier.append(queue.get())

    # Return an empty list if the path is not found
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


def initialize_algorithm(start: Position) -> tuple[PriorityQueue[Node], set[Node], int, list[Node]]:
    """
    This function is used to initialize anything that is needed for all of our algorithms to run.
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param distance: the initial distance between the start node and the end node
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    Returns: a tuple of the priority queue, the explored set, and the depth
    """
    queue: PriorityQueue[Node] = PriorityQueue()
    queue.put(Node.worldmap_reference[start[0], start[1]])
    return queue, set(), 0, []


def neighbors(current_node: Node, explored: set[Node]) -> list[Node]:
    """
    This function is used to get the neighbors of the current node that can be explored.
    :param current_node: the current node
    :param explored: the explored set
    Returns: a list of nodes that represents the neighbors of the current node that can be explored
    """
    neighbor_nodes = current_node.get_neighbors()
    remove_nodes = []
    for node in neighbor_nodes:
        if not node.traversable():
            continue
        if node in explored:
            continue
        remove_nodes.append(node)
    return remove_nodes


def backtrack(back_path: list[Node]) -> list[Position]:
    """
    This function is used to backtrack from the last node to the first node.
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    path = []
    for node in back_path:
        path.append(node.get_coordinates())
    return path


T = TypeVar('T')


def queue_to_str(queue: PriorityQueue[T]) -> str:
    """
    Iterates over PriorityQueue and prints out the __str__ of each element.

    Parameters
    ----------
    queue : PriorityQueue[T]
        A Generic PriorityQueue

    Returns
    -------
    str
        A combination of the __str__ of each element
    """
    string = ''
    for element in queue.queue:
        string.join(f'{element} ')

    return string
