# Robotics-Final-Project

# Algorithms:

**1) A\***
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

## 1) Greedy:
[Manhattan](https://youtu.be/X4M8PvoTzAQ)

[Euclidean](https://youtu.be/D5H7L5vYMzI)

[Chebyshev](https://youtu.be/Cp9DrXKQI-w)

[Octile](https://youtu.be/lyZvc4FDa54)

[Bozo](https://youtu.be/Iguz9JbiYVQ)

## 2) A\*
[Manhattan](https://youtu.be/WIc21hOAth8)

[Euclidean](https://youtu.be/3u1lxfqrvY4)

[Chebyshev](https://youtu.be/WCrXmY2Jtw4)

[Octile](https://youtu.be/QiEmjwGPaGU)

[Bozo](https://youtu.be/biGdXdjMwMc)

[Diagonal](https://youtu.be/IwjQEz6H3CE)

## 3) Djikstra:
[Djikstra](https://youtu.be/LYqw2WOBfUY)

## 4) Bea:
[Beam](https://youtu.be/MGI7nls11og)
