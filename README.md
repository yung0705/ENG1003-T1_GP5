# ENG1003-T1_GP5
GitHub Readme.md Report

## 1.Background of path planning

## 2.Theory of Path Planning Algorithm
Path planning has three components: spatial representation, search algorithm and heuristic algorithm.

Spatial representation means constructing a map environment for the target before executing the path planning. To perform any type of path planning, you need to discretize the map environment into graphics. In order to improve the effect of path planning, the map environment can be expressed as several special graphics, including: navigation grid, waypoint map and grid map. The navigation grid is a special type of graphics abstracted from the real world. In short, the navigation grid can be defined as a set of convex polygons, used to constrain the range that the target can move in this environment. The waypoint diagram abstracts the real world into another representation in path planning. The waypoint graph is composed of nodes at different locations on the map. These nodes are connected by straight lines and can be traversed on these straight lines. The waypoint map is usually designed by the user, which requires a lot of adjustments to make the search effective. It has a great effect on the image of enclosed space. The grid is the most commonly used graphic structure to represent the real world. A grid is a graphic composed of repeated squares or a group of squares called edges, used to represent the topography of the map. Grids can be quickly and efficiently generated to represent the environment, and are used extensively in path search research to test new algorithms.

There are many search algorithms that can work on the graph to find the target node from the starting node. The search algorithms used by some early researchers are BFS (breadth first search), DFS (depth first search) and iterative deep search. These methods can often find the required path, but the efficiency is very low, because they can be boiled down to brute force algorithms, and every path that may exist on the graph must be traversed. In order to provide a more intelligent and intuitive search environment method, an informed search algorithm came into being. Dijkstra algorithm is an informed search algorithm used to solve the single source shortest path problem. It calculates the cost of traversing from one node to another node to the target node in real time and selects the path with the lowest cost. Similarly, the best priority search calculates the lowest cost required for each node from the current node to the next node, instead of calculating the cost of various paths in real time during the entire traversal process. The A* algorithm is produced by fusing the attributes of Dijkstra and the best first search.

Heuristics are the cornerstone of modern path planning. They provide the search algorithm with the ability to calculate the cost from the initial node to the target node. Heuristic algorithms provide a lot of help for humans and machines in making decisions and solving problems. In the path planning problem, there are two classic heuristic algorithms to solve specific situations, including Manhattan distance and Euclidean distance. The definition of Manhattan distance is the distance between two points in the grid in the Cartesian coordinate system. This heuristic was inspired by the Manhattan urban road network that looks a lot like a grid layout. The heuristic Euclidean distance is defined as the straight-line distance between two points on the grid. In the plane space, this heuristic is defined as Pythagoras' theorem.

## 3.Introduction of the Engineering Tools
Python was designed in the early 1990s by Guido van Rossum of the Dutch Society of Mathematics and Computer Science Research as an alternative to the ABC language. Python provides efficient high-level data structures, as well as simple and effective object-oriented programming. Python syntax and dynamic typing, as well as the nature of interpreted languages, make it a programming language for scripting and rapid application development on most platforms. With the continuous update of the version and the addition of new language features, it has gradually been used for independent, large-scale applications.

GitHub is an open-source hosting service, a bit like a cloud of code. It hosts your source code projects in a variety of different programming languages and tracks the various changes made in each iteration. The service can do this by using git, a revision control system that runs in a command line interface. 

## 4.Tutorial Task
In the tutorial task, we have to create four functions and combine it into one big function by creating a main function. So, when we call that function number, and the function will show it out. My work is to create the main function to combine my groupmate function together. Before I show the main function, let us have a look at the functions that my groupmates have done:

### Function 1：(from Man)
Code：
```
x = int(input("Height: "))
for num in range(x):
    print("XXX")
```
In function 1, we create a function that is a tower builder. Ask for an integer for the height, and generate the number of rows with xxx, shown below

If input “1”
Then it will output:
xxx

If input “2”
Then it will output
xxx
xxx
.
![2021-11-12 (4)](https://user-images.githubusercontent.com/89887457/141357278-211c75e2-e7a6-4c80-924e-2aa3a84a5020.png)

### Function 2：(from Ethan)
Code：
```
a = int(input('First number: '))
b = int(input('Second number: '))
print('The sum is',a+b)
```
In function 2, we have to let the user input two integers and sum them up like shown as below:
![2021-11-12 (5)](https://user-images.githubusercontent.com/89887457/141357865-04767e3e-1e98-4d65-bac6-5cc07c498a2c.png)

### Function 3：(from James)
Code：
```
x = int(input("List length: "))
for num in range(x):
    print(x-num)
```
In function 3, we have to input an integer. Then the programe will output a descending order integer list which is from the integer you input to 1, as shown below:
![2021-11-12 (6)](https://user-images.githubusercontent.com/89887457/141360682-c96e9d5a-7e78-437a-92a8-1b59ad69043a.png)

### Function 4：(from Mielsen)
Code：
```
x = int(input("Square Size:"))
for num in range(x): 
    for num in range(x): 
        print("[]",end="")
    print()
```
In function 4, input the size of the square and the programe will print it out using [] as a building block, like shown below:
![2021-11-12 (7)](https://user-images.githubusercontent.com/89887457/141362433-f699c7f5-557c-471f-a6a8-857938ae6dfd.png)
I used two for-loop. first one is for the y-axis, second one is for the x-axis. Also, i added [end=""] to make the block, which should be on the same line, is the right position, if not, the block will automatically print on the next line.

### Function 5：(from Mielsen)
Code：
```
import random
print("Number Guessing Game")
lower = 1
upper = random.randint(50,200)
print("The range for this round is ",lower,"-",upper)
x = random.randint(lower, upper)
attempts = 0
guess = 0
while x != guess:	
	guess = int(input("Make a guess : "))
	if x > guess:
		lower = guess
		print("The range is now ",lower,"-",upper)
		attempts = attempts + 1
	if x < guess:
		upper = guess
		print("The range is now ",lower,"-",upper)
		attempts = attempts + 1
else:
	attempts = attempts + 1
	print("BINGO! You took ",attempts," attempts to reach the answer!")
```
Function 5 is a number guessing game. When the function starts running, it will generate an integer randomly by using the "random" command from the "random" module. Then it will show the guessing range. You can input integers to guess. If it is incorrect, the range will update and you can guess again until the answer is correct. At the end, the programe will tell you the number of trying
![2021-11-12 (8)](https://user-images.githubusercontent.com/89887457/141371600-35740087-5d22-4d16-8b70-03bc459662c6.png)

### Main function：(from Iassc)
Code：
```
def function1():
    x = int(input("Height: "))
    for num in range(x):
        print("XXX")

def function2():
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print('The sum is',a+b)
    
def function3():
    y = int(input("List length: "))
    for num in range(y):
        print(y-num)

def function4():
    z = int(input("Square Size:"))
    for num in range(z): 
        for num in range(z): 
            print("[]",end="")
        print()

def function5():
    import random
    print("Number Guessing Game")
    lower = 1
    upper = random.randint(50,200)
    print("The range for this round is ",lower,"-",upper)

    c = random.randint(lower, upper)
    attempts = 0
    guess = 0

    while c != guess:	
    	guess = int(input("Make a guess : "))
    	if c > guess:
    		lower = guess
    		print("The range is now ",lower,"-",upper)
    		attempts = attempts + 1
    	if c < guess:
    		upper = guess
    		print("The range is now ",lower,"-",upper)
    		attempts = attempts + 1
    else:
	    attempts = attempts + 1
	    print("BINGO! You took ",attempts," attempts to reach the answer!")

print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
elif inp == '5':
    function5()
else:
    print('There is no function. Please enter(1-5)')
```
In main function, I have to create a main function so that we can call that particular function directly. For preventing error, I renamed the variables which appear in different functions at the same time.
