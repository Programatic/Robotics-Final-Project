# Robotics-Final-Project

# Algorithms:

**1) A***
This algorithm guarantees to find the shortest path if it exists. The algorithm uses a priority queue to sort the nodes by distance to the node + distance chosen by a heuristic to the goal.

Runtime:

Space Complexity:

**2) Greedy-First Search (aka. Best-First Search)**
This algorithm prioritizes getting to the goal as quickly as possible. The algorithm uses a priority queue to sort the nodes by distance chosen by a heuristic to the goal. This algorithm is not guaranteed to find the shortest path.

Runtime:

Space Complexity:

**3) Beam**
Beam search is an optimized version of Greedy-First Search that reduces the memory requirements of Best-First Search. At each depth level, the algorithm sorts all of the neighbors and then only stores the k-best nodes at each level.

Runtime:
Space Complexity:

**4) Djikstra**
This algorithm prioritizes nodes that are closer to the current node.

Runtime:
Space Complexity:
