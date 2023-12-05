"""
The entrypoint for the project.
"""
import sys
from typing import Optional

from coppeliasim_zmqremoteapi_client import RemoteAPIClient  # type: ignore

from node import HeuristicFunction, Node
import heuristic
import search
import utils as util

# pylint: disable=invalid-name
# This part is from assignment2_part1.py from the homework
# if __name__ == "__main__":
client = RemoteAPIClient()
sim = client.getObject("sim")

worldmap = util.GridMap(sim, 5.0)
worldmap.inflate_obstacles(num_iter=8)
worldmap.normalize_map()

goal = sim.getObjectHandle("/goal_point")  # pylint: disable=no-member
goal_world = sim.getObjectPosition(goal, sim.handle_world)  # pylint: disable=no-member
goal_grid = worldmap.get_grid_coords(goal_world)

robot = sim.getObjectHandle("/PioneerP3DX")  # pylint: disable=no-member
start_world = sim.getObjectPosition(robot, sim.handle_world)  # pylint: disable=no-member
start_grid = worldmap.get_grid_coords(start_world)

start = tuple(start_grid)[::-1]
Node.end_coordinate = tuple(goal_grid)[::-1]

algorithm = None
heuristic_choice = None
diagonal_neighbors = False
depth_limit = 1000000
try:
    algorithm = sys.argv[1]
    heuristic_choice = sys.argv[2]
    diagonal_neighbors = bool(sys.argv[3])
    depth_limit = int(sys.argv[4])
except IndexError:
    print("Not all arguments so using some default values.")
    print(depth_limit)

heuristic_func: Optional[HeuristicFunction] = None

match algorithm:
    case "a_star":
        search_func = search.a_star
    case 'greedy_first':
        Node.cost_addition = 0
        search_func = search.a_star
        # search_func = search.greedy_first
    case 'beam':
        search_func = search.beam # type: ignore
        Node.cost_addition = 0
    # case 'brushfire':
        # search_func = search.brushfire
    case 'djikstra':
        heuristic_func = heuristic.no_heuristic
        search_func = search.a_star
    case _:
        print("Using default search A*.")
        search_func = search.a_star

if heuristic_func:
    print("Chosen Djikstra so no heuristic function.")
else:
    match heuristic_choice:
        case 'manhattan':
            heuristic_func = heuristic.manhattan_distance
        case 'euclidean':
            heuristic_func = heuristic.euclidean_distance
        case 'chebyshev':
            heuristic_func = heuristic.chebyshev_distance
        case 'octile':
            heuristic_func = heuristic.octile_distance
        case 'bozo':
            heuristic_func = heuristic.bozo_distance
        case _:
            print("Using default heuristic manhattan distance.")
            heuristic_func = heuristic.manhattan_distance

Node.worldmap_reference = worldmap.world_to_nodes(heuristic_func)
assert Node.worldmap_reference is not None

Node.diagonal_neighbors = diagonal_neighbors

print("Starting Search")
path = search_func(start, depth_limit)

if not path:
    print("No path found.")
    sys.exit(0)

trace_world = worldmap.get_world_coords(path)
coppelia_path = util.generate_path_from_trace(sim, trace_world, 100)

trackpoint = sim.getObjectHandle("/track_point")  # pylint: disable=no-member
util.execute_path(coppelia_path, sim, trackpoint, robot, thresh=0.1)
