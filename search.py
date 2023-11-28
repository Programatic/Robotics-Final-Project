"""
This file contains the search algorithms that are used to find the path from the start node to the end node
"""
from queue import PriorityQueue
from typing import Callable, Optional
from node import Node, Position

# (x, y) coordinates of the maze's start and end
# TO DO: Change this to the start coordinates of the maze
start_coordinates: Position = (0, 0)
# TO DO: Change this to the end coordinates of the maze
end_coordinates: Position = (100, 100)


def a_star(heuristic: Callable[[Position, Position], int],
           diagonal_neighbors: bool = False, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """

    # Initialize the frontier set, the explored set, and the depth
    frontier, depth = initialize_algorithm(heuristic, diagonal_neighbors)
    explored = set()

    # Initialize the priority queue
    queue = PriorityQueue()
    queue.put((frontier[0], frontier[0].start_distance + frontier[0].goal_distance))

    # While the frontier is not empty
    while not queue.empty() and depth < depth_limit:
        # Update the depth
        depth += 1

        # Get the current node and add it to the explored set
        current_node = queue.get()[0]
        explored.add(current_node)

        # If the current node is the goal node
        if current_node == end_coordinates:
            return backtrack(current_node)

        # Get the neighbors of the current node that can be explored
        neighbors = current_node.get_neighbors()
        neighbors[:] = [neighbor for neighbor in neighbors if neighbor not in explored]
        neighbors[:] = [neighbor for neighbor in neighbors if neighbor.traversable()]

        # Add the neighbors to the frontier
        queue.put((neighbor, neighbor.start_distance + neighbor.goal_distance) for neighbor in neighbors)

    return []


def greedy_first(heuristic: Callable[[Position, Position], int],
                 diagonal_neighbors: bool = False, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the frontier set, the explored set, and the depth
    frontier, depth = initialize_algorithm(heuristic, diagonal_neighbors)
    explored = set()

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


def beam(heuristic: Callable[[Position, Position], int], k: int = 2,
         diagonal_neighbors: bool = False, depth_limit: int = 50) -> list[Position]:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param k: the number of nodes to keep in the frontier
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # Initialize the frontier set and the depth
    frontier, depth = initialize_algorithm(heuristic, diagonal_neighbors)

    # While the frontier is not empty
    while frontier and depth < depth_limit:
        # Update the depth
        depth += 1

        next_frontier = []

        # Add the neighbors to the frontier
        for node in frontier:
            # If the current node is the goal node
            if node == end_coordinates:
                return backtrack(node)

            # Otherwise, add the traversable neighbors to the next frontier
            next_frontier.extend([neighbor for neighbor in node.get_neighbors() if neighbor.traversable()])

        # Sort the next frontier by their heuristic value
        next_frontier.sort(key=lambda neighbor: neighbor.goal_distance)

        # Set the frontier to the best k nodes in next frontier
        frontier = next_frontier[:k]

    # Return an empty list if the path is not found
    return []


def brushfire(heuristic: Callable[[Position, Position], int],
              diagonal_neighbors: bool = False, depth_limit: int = 50) -> list['Node']:
    """
    :param heuristic: the heuristic function to use for calculating the distance between two nodes
    :param diagonal_neighbors: whether diagonal neighbors are allowed
    :param depth_limit: the depth limit of the search
    Returns: a list of nodes that represents the path from the start node to the end node
    """
    # TO DO: Implement this function
    heuristic(start_coordinates, end_coordinates)
    if diagonal_neighbors:
        depth_limit = max(heuristic(start_coordinates, end_coordinates), depth_limit)
    return []


def initialize_algorithm(heuristic: Callable[[Position, Position], int],
                         diagonal_neighbors: bool = False) -> tuple[list['Node'], int]:
    """
    This function is used to initialize anything that is needed for all of our algorithms to run.
    Returns: a tuple of a list of nodes containing the start node and the depth as 0
    """
    return [Node(pos=start_coordinates, destination=end_coordinates, heuristic_function=heuristic,
                 diagonal_neighbors=diagonal_neighbors)], 0


def backtrack(last_node: Optional[Node]) -> list[Position]:
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
