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

## 4) Beam:
[Beam](https://youtu.be/MGI7nls11og)

# Performance

| Algorithm          	| Time (ms) 	| Memory Usage (KiB) 	| Path Length 	|
|:--------------------|----------:	|-------------------:	|------------:	|
| Greedy - Manhattan 	|      8.77 	|              35.02 	|         443 	|
| Greedy - Euclidean 	|      8.99 	|              16.50 	|         445 	|
| Greedy - Chebyshev 	|     12.15 	|              39.41 	|         440 	|
| Greedy - Octile    	|      9.48 	|              18.38 	|         440 	|
| Greedy - Bozo      	|    467.63 	|              87.52 	|         920 	|
| A\* - Manhattan    	|    139.06 	|             355.35 	|         406 	|
| A\* - Euclidean    	|    325.76 	|             922.16 	|         406 	|
| A\* - Chebyshev    	|    313.34 	|             740.43 	|         406 	|
| A\* - Octile       	|    316.32 	|             869.81 	|         406 	|
| A\* - Bozo         	|    488.43 	|            1887.28 	|         594 	|
| A\* - Diagonals    	| 651.65    	| 893.56             	| 400.66      	|
| Djikstra           	|    597.88 	|           14767.47 	|         407 	|
| Beam               	|     88.70 	|             194.20 	|         406 	|
