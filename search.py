"""
This file contains the search algorithms that are used to find the path from the start node to the end node
"""
from queue import PriorityQueue
from typing import Optional
import heapq

from node import Node, Position
import utils as util


# pylint: disable=too-many-locals
def djikstra(start: Position, depth_limit: int = 10000) -> list[Position]:
    '''
    :param start: Start position to run djikstra with
    :param iterations: Number of iterations to allow djikstra to run
    Returns a list of Positions of the path if possible
    '''
    graph = Node.worldmap_reference
    rows, cols = len(graph), len(graph[0])

    # Initialize distances and predecessors
    distances = {(i, j): float("infinity") for i in range(rows) for j in range(cols)}
    distances[start] = 0
    predecessors: dict[Position, Optional[Node]] = {
        (i, j): None for i in range(rows) for j in range(cols)
    }

    priority_queue = [(0, Node.worldmap_reference[start[0], start[1]])]

    i = 0
    while priority_queue and i < depth_limit:
        i += 1
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        neighbors = current_node.get_neighbors()

        for neighbor in neighbors:
            ni, nj = neighbor.pos[0], neighbor.pos[1]

            if 0 <= ni < rows and 0 <= nj < cols:
                distance = current_distance + 1

                if distance < distances[(ni, nj)]:
                    distances[(ni, nj)] = distance
                    predecessors[(ni, nj)] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    def get_shortest_path(
        predecessors: dict[Position, Optional[Node]],
        start: Position,
        destination: Position,
    ) -> list[Position]:
        path: list[Position] = []
        current_node = destination

        if predecessors[current_node] is None:
            return []

        while current_node is not None:
            if isinstance(current_node, Node):
                path.insert(0, (current_node.pos[0], current_node.pos[1]))
            else:
                path.insert(0, current_node)

            current_node = predecessors[current_node]  # type: ignore

        if path[0] != start:
            return []

        return path

    return get_shortest_path(predecessors, start, Node.end_coordinate)


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
