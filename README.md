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

## 5.Compulsory Task 1
### Methodology：
In this task, we need to find the PolyU Aircraft Model (PolyU-A380, PolyU-A381, PolyU-A382, PolyU-A383) that achieves minimum cost with the respective map.As data shown below:
![圖片1](https://user-images.githubusercontent.com/89887457/141405572-049e1a17-8caa-464e-84fd-c3c1660ffe5c.png)![圖片2](https://user-images.githubusercontent.com/89887457/141405616-f65577f8-ebe4-48e2-9434-c7c33bfd5e97.png)
#### Starting point and goal node：
According to the map shown above, “S” indicates the starting point of the airplane where the plane takes off, which is (0, 50) in coordinate form. Therefore, we have input the “sx” (x-coordinate of starting point) as 0 and “sy” (y-coordinate of starting point) as 50; Identically, “E” indicates the goal note of the airplane where the airplane lands, which is (50, -5) in coordinate form. Therefore, we have input the “gx” (x-coordinate of goal point) as 50 and “gy” (y-coordinate of goal point) as -5.
```
    sx = 0.0
    sy = 50.0
    gx = 50.0
    gy = -5.0
```
![螢幕擷取畫面 2021-11-12 115653](https://user-images.githubusercontent.com/89887457/141406719-4259ec4e-701a-450d-b2bb-f7188c21e916.png)

#### Boundary line：
We need to also draw two boundary lines that we cannot directly passes through like a wall. The two lines are created by the code below:
```
    for i in range(50): # draw the free border
        ox.append(10)
        oy.append(60-i)
    for i in range(-10, 50):
        ox.append(35)
        oy.append(i)
```
![螢幕擷取畫面 2021-11-12 120731](https://user-images.githubusercontent.com/89887457/141407687-d9d2d218-f196-4a9a-90ee-0f6d3103a1d2.png)

As a line is created by many dots, we used "for-loop" to generate numbers of continuous dots in a direction. The length of the border depends on the range of the for-loop, for example ```for i in range(50): ``` means that there will be a 50 grid points long border. Also, "ox" and "oy" represent the x-coordinate and the y-coordinate of the border respectively

#### Fuel & time consumption area：
According to the path planning map above, the greenish yellow area and red area indicates the fuel consumption area and the time consumption area respectively. When the aircraft go through that area, the total cost of the flight will increase. The fuel consumption area is created by the code below:
```
    fc_x, fc_y = [], []
    for i in range(15, 30):
        for j in range(20, 40):
            fc_x.append(i)
            fc_y.append(j)
```
The time consumption area is created by the code below:
```
    tc_x, tc_y = [], []
    for i in range(40, 55):
        for j in range(25, 45):
            tc_x.append(i)
            tc_y.append(j)
```
![螢幕擷取畫面 2021-11-12 125446](https://user-images.githubusercontent.com/89887457/141411951-7f39e5c7-81b3-46d9-8db8-a3a8c0f17ff4.png)


Their code are similar to the code of the border. The main difference is that there is one more "for-loop". So the programe can generate continuous dots in two directions to make a rectangle.

#### Aircraft Models
In this task, we also need to find out which type of model aircraft achieves the minimum flight cost. In the A-Star Path Planning Algorithm, there are 7 variables which will affect the total flight cost. They are C_F, Delta_F, C_T, Delta_T, C_C, Delta_F_A, Delta_T_A. So, we need to change those variables to match the different aircraft models.

### Result：

### Discussion：

## 6.Compulsory Task 2.1
### Methodology：

### Result：

### Discussion：

## 7.Compulsory Task 2.2
### Methodology：

### Result：

### Discussion：

## 8.Compulsory Task 3
### Methodology：
The goal of this task is to design a new cost area that can reduce the cost. Before adding code, I need to understand the original code. First, I need to set new attributes of AStarPlanner, which are minus_cost_x, minus_cost_y, C_P, and Delta_P. Then, I need to add ```+self.C_P*self.Delta_P``` to the cost-calculating equation for this new area.
![螢幕擷取畫面 2021-11-10 185614](https://user-images.githubusercontent.com/89887457/141402794-795b78c4-e84d-4518-b386-01362e1d1706.png)
![螢幕擷取畫面 2021-11-10 185839](https://user-images.githubusercontent.com/89887457/141402758-0be1c4ec-cb54-4e8a-b66b-8081e3bdcb7f.png)

Also, I need to change the motion model because more things need to be calculated. For the new situation, which is when the aircraft goes through the minus-cost area, I added
```
if self.calc_grid_position(node.x, self.min_x) in self.minus_cost_x:
	if self.calc_grid_position(node.y, self.min_y) in self.minus_cost_y:
		node.cost = node.cost - self.Delta_P * self.motion[i][2]
```
![螢幕擷取畫面 2021-11-10 190047](https://user-images.githubusercontent.com/89887457/141403233-0bbde9e6-9151-42b7-a782-7b4846a0cc20.png)

. That all of the calculating part.
The map generation part is the next challenge. First, I added 
```
minus_cost_x , minus_cost_y = [], []
for i in range(37,38):
	for j in range(29,45):
		minus_cost_x.append(i)
			minus_cost_y.append(j)
```
and
```
plt.plot(minus_cost_x, minus_cost_y, "ob")
```
![螢幕擷取畫面 2021-11-10 190428](https://user-images.githubusercontent.com/89887457/141403254-ad60e690-9905-495b-b683-5c380319fb87.png)

. The first code is about the size and the location of the area.  "i" is x coordinate, and "j" is y coordinate. The maximum size of the area is limited, 16 grid points, and for the best location of the area so the range of "i" and "j" need to be designed. After trial and error, 37 to 38 seem suitable to be the range of "i", 29 to 45 seem suitable to be the range of "j". The second code is necessary for printing the area on the map. It can also design the pattern and color of the area. In the end, A blue minus-cost area is shown on the map, and when the aircraft goes through the area, the cost will be reduced.

### Result：
After designed a suitable location for the minus-cost area to make it minimizes the cost as much as possible. The cost from 3356.469824904021
![2021-11-12 (1)](https://user-images.githubusercontent.com/89887457/141403346-33105142-4a8e-4adf-82e9-7df8434566a4.png)
decreased to 2685.6271124294003
![2021-11-12](https://user-images.githubusercontent.com/89887457/141403338-971fbe20-4699-4166-b3f6-975cb3c5b51b.png)

### Discussion：
We think the difficult part of this task is that we need to read and understand the code. It is because this task is different from previous tasks. In this task, we are not only changing the numbers but also adding some new code. So understanding the code is necessary for preventing errors and incorrect outcomes. For example, in line 167, if I just follow the code from line 156 or 162, we can see that the path is evading the minus-cost area. This result does not make sense.
![螢幕擷取畫面 2021-11-12 112220](https://user-images.githubusercontent.com/89887457/141403676-8edd2584-f65b-45d3-a521-f9fc40ad03a9.png)

For the minimum cost, the aircraft should go through that area. After researching, I found that in line 167 the sign between "node.cost" and "self.Delta_P" should be "-"
```
node.cost = node.cost - self.Delta_P * self.motion[i][2]
```
. Then, the result will be correct
