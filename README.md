# ENG1003-T1_GP5
GitHub Readme.md Report

#1.Background of path planning:






#2. (Ethan Li)
Path planning has three components: spatial representation, search algorithm and heuristic algorithm.

Spatial representation means to construct a map environment for the target before executing the path planning. To perform any type of path planning, you need to discretize the map environment into graphics. In order to improve the effect of path planning, the map environment can be expressed as several special graphics, including: navigation grid, waypoint map and grid map. Navigation grid is a special type of graphics abstracted from the real world. In short, the navigation grid can be defined as a set of convex polygons, used to constrain the range that the target can move in this environment. The waypoint diagram abstracts the real world into another representation in path planning. The waypoint graph is composed of nodes at different locations on the map. These nodes are connected by straight lines and can be traversed on these straight lines. The waypoint map is usually designed by the user, which requires a lot of adjustments to make the search effective. It has great effect on the image of enclosed space. The grid is the most commonly used graphic structure to represent the real world. A grid is a graphic composed of repeated squares or a group of squares called edges, used to represent the topography of the map. Grids can be quickly and efficiently generated to represent the environment, and are used extensively in path search research to test new algorithms.

There are many search algorithms that can work on the graph to find the target node from the starting node. The search algorithms used by some early researchers are BFS (breadth first search), DFS (depth first search) and iterative deep search. These methods can often find the required path, but the efficiency is very low, because they can be boiled down to brute force algorithms, and every path that may exist on the graph must be traversed. In order to provide a more intelligent and intuitive search environment method, an informed search algorithm came into being. Dijkstra algorithm is an informed search algorithm used to solve the single source shortest path problem. It calculates the cost of traversing from one node to another node to the target node in real time, and selects the path with the lowest cost. Similarly, the best priority search calculates the lowest cost required for each node from the current node to the next node, instead of calculating the cost of various paths in real time during the entire traversal process. The A* algorithm is produced by fusing the attributes of Dijkstra and the best first search.

Heuristics are the cornerstone of modern path planning. They provide the search algorithm with the ability to calculate the cost from the initial node to the target node. Heuristic algorithms provide a lot of help for humans and machines in making decisions and solving problems. In the path planning problem, there are two classic heuristic algorithms to solve specific situations, including Manhattan distance and Euclidean distance. The definition of Manhattan distance is the distance between two points in the grid in the Cartesian coordinate system. This heuristic was inspired by the Manhattan urban road network that looks a lot like a grid layout. The heuristic Euclidean distance is defined as the straight-line distance between two points on the grid. In the plane space, this heuristic is defined as Pythagoras' theorem.

#3. (Ethan Li)
a) Python was designed in the early 1990s by Guido van Rossum of the Dutch Society of Mathematics and Computer Science Research as an alternative to the ABC language. Python provides efficient high-level data structures, as well as simple and effective object-oriented programming. Python syntax and dynamic typing, as well as the nature of interpreted languages, make it a programming language for scripting and rapid application development on most platforms. With the continuous update of the version and the addition of new language features, it has gradually been used for independent, large-scale applications.

b) GitHub is an open-source hosting service, a bit like a cloud of code. It hosts your source code projects in a variety of different programming languages and tracks the various changes made in each iteration. The service can do this by using git, a revision control system that runs in a command line interface. 



