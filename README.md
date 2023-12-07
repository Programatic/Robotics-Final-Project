# Robotics-Final-Project

# Algorithms:

**1) A***
This algorithm guarantees to find the shortest path if it exists. The algorithm uses a priority queue to sort the nodes by distance to the node + distance chosen by a heuristic to the goal.

Runtime: O(d log b)
Space Complexity: O(b)

**2) Greedy-First Search (aka. Best-First Search)**
This algorithm prioritizes getting to the goal as quickly as possible. The algorithm uses a priority queue to sort the nodes by distance chosen by a heuristic to the goal. This algorithm is not guaranteed to find the shortest path.

Runtime: O(d log b)
Space Complexity: O(b)

**3) Beam**
Beam search is an optimized version of Greedy-First Search that reduces the memory requirements of Best-First Search. At each depth level, the algorithm sorts all of the neighbors and then only stores the k-best nodes at each level.

Runtime: O(d * k log k)
Space Complexity: O(k)

**4) Djikstra**
This algorithm prioritizes nodes that are closer to the current node.

Runtime: O(d log b)
Space Complexity: O(b)

# Heuristics: 
All videos for the heuristics are shown using the Greedy algorithm

**1) Manhattan:** Δx + Δy
https://youtu.be/X4M8PvoTzAQ

**2) Euclidean:** sqrt(Δx^2 + Δy^2)
https://youtu.be/D5H7L5vYMzI

**3) Chebyshev:** max(Δx, Δy)
https://youtu.be/Cp9DrXKQI-w

**4) Octile:** Δx + Δy + (2^0.5 - 2) * min(Δx, Δy)
https://youtu.be/lyZvc4FDa54
