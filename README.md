# ENG1003-T1_GP5
GitHub Readme.md Report
## Presentation
https://drive.google.com/file/d/1njAntgKOZxLf-Ph7eNCHOChekKgX-NRb/view?usp=sharing
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
    <li><a href="README.md#1background-of-path-planning">1.Background of path planning</a></li>
    <li><a href="README.md#2theory-of-path-planning-algorithm">2.Theory of Path Planning Algorithm</a></li>
    <li><a href="README.md#3introduction-of-the-engineering-tools">3.Introduction of the Engineering Tools</a></li>
    <li><a href="README.md#4tutorial-task">4.Tutorial Task</a></li>
    <li><a href="README.md#5compulsory-task-1">5.Compulsory Task 1</a></li>
    <li><a href="README.md#6compulsory-task-21">6.Compulsory Task 2.1</a></li>
    <li><a href="README.md#7compulsory-task-22">7.Compulsory Task 2.2</a></li>
    <li><a href="README.md#8compulsory-task-3">8.Compulsory Task 3</a></li>
    <li><a href="README.md#9reflective-essay">9.Reflective Essay</a></li>
    <li><a href="README.md#10references">10.References</a></li>
  </ol>
</details>

## 1.Background of path planning
Path planning is an important primitive of autonomous mobile robots, which allows the robot to find the shortest or best path between two points. In aviation engineering, it also occupies a very important position, such as reducing fuel costs and passenger risks. 

Path planning requires the environment map and the robot to understand its position relative to the map. We now assume that the robot can locate itself, be equipped with a map, and be able to avoid temporary obstacles on the way. When designing a route, you must also understand how to create a map, how to locate the robot, and how to deal with uncertain location information. One of the earliest and simplest algorithms is Dijkstra's algorithm. Starting from the initial vertex where the path should start, the algorithm marks all direct neighbors of the initial vertex with the cost of getting there. Then it continues from the vertex with the lowest cost to all its neighboring vertices, and if the cost is lower, it marks them as the cost of reaching them by themselves. Once all neighbors of the vertex have been checked, the algorithm will continue to the vertex with the next lowest cost. Once the algorithm reaches the target vertex, it terminates and the robot can proceed along the edge that points to the lowest edge cost. 

The Dijkstra algorithm is one of the most commonly used path planning algorithms and is also applied to route planning. This is also one of the necessary knowledge we learned in the course.

## 2.Theory of Path Planning Algorithm
Path planning has three components: spatial representation, search algorithm and heuristic algorithm.

Spatial representation means constructing a map environment for the target before executing the path planning. To perform any type of path planning, you need to discretize the map environment into graphics. In order to improve the effect of path planning, the map environment can be expressed as several special graphics, including: navigation grid, waypoint map and grid map. The navigation grid is a special type of graphics abstracted from the real world. In short, the navigation grid can be defined as a set of convex polygons, used to constrain the range that the target can move in this environment. The waypoint diagram abstracts the real world into another representation in path planning. The waypoint graph is composed of nodes at different locations on the map. These nodes are connected by straight lines and can be traversed on these straight lines. The waypoint map is usually designed by the user, which requires a lot of adjustments to make the search effective. It has a great effect on the image of enclosed space. The grid is the most commonly used graphic structure to represent the real world. A grid is a graphic composed of repeated squares or a group of squares called edges, used to represent the topography of the map. Grids can be quickly and efficiently generated to represent the environment, and are used extensively in path search research to test new algorithms.

There are many search algorithms that can work on the graph to find the target node from the starting node. The search algorithms used by some early researchers are BFS (breadth first search), DFS (depth first search) and iterative deep search. These methods can often find the required path, but the efficiency is very low, because they can be boiled down to brute force algorithms, and every path that may exist on the graph must be traversed. In order to provide a more intelligent and intuitive search environment method, an informed search algorithm came into being. Dijkstra algorithm is an informed search algorithm used to solve the single source shortest path problem. It calculates the cost of traversing from one node to another node to the target node in real time and selects the path with the lowest cost. Similarly, the best priority search calculates the lowest cost required for each node from the current node to the next node, instead of calculating the cost of various paths in real time during the entire traversal process. The A* algorithm is produced by fusing the attributes of Dijkstra and the best first search.

Heuristics are the cornerstone of modern path planning. They provide the search algorithm with the ability to calculate the cost from the initial node to the target node. Heuristic algorithms provide a lot of help for humans and machines in making decisions and solving problems. In the path planning problem, there are two classic heuristic algorithms to solve specific situations, including Manhattan distance and Euclidean distance. The definition of Manhattan distance is the distance between two points in the grid in the Cartesian coordinate system. This heuristic was inspired by the Manhattan urban road network that looks a lot like a grid layout. The heuristic Euclidean distance is defined as the straight-line distance between two points on the grid. In the plane space, this heuristic is defined as Pythagoras' theorem.

## 3.Introduction of the Engineering Tools
Python was designed in the early 1990s by Guido van Rossum of the Dutch Society of Mathematics and Computer Science Research as an alternative to the ABC language. Python provides efficient high-level data structures, as well as simple and effective object-oriented programming. Python syntax and dynamic typing, as well as the nature of interpreted languages, make it a programming language for scripting and rapid application development on most platforms. With the continuous update of the version and the addition of new language features, it has gradually been used for independent, large-scale applications.

GitHub is an open-source hosting service, a bit like a cloud of code. It hosts your source code projects in a variety of different programming languages and tracks the various changes made in each iteration. The service can do this by using git, a revision control system that runs in a command line interface. 

## 4.[Tutorial Task](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/Tutorial%201.py)
In the tutorial task, we have to create four functions and combine it into one big function by creating a main function. So, when we call that function number, and the function will show it out. My work is to create the main function to combine my groupmate function together. Before I show the main function, let us have a look at the functions that my groupmates have done:

### [Function 1](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/function_1.py)：(from Man)
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

### [Function 2](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/function_2.py)：(from Ethan)
Code：
```
a = int(input('First number: '))
b = int(input('Second number: '))
print('The sum is',a+b)
```
In function 2, we have to let the user input two integers and sum them up like shown as below:
![2021-11-12 (5)](https://user-images.githubusercontent.com/89887457/141357865-04767e3e-1e98-4d65-bac6-5cc07c498a2c.png)

### [Function 3](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/function_3.py)：(from James)
Code：
```
x = int(input("List length: "))
for num in range(x):
    print(x-num)
```
In function 3, we have to input an integer. Then the programe will output a descending order integer list which is from the integer you input to 1, as shown below:
![2021-11-12 (6)](https://user-images.githubusercontent.com/89887457/141360682-c96e9d5a-7e78-437a-92a8-1b59ad69043a.png)

### [Function 4](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/function_4.py)：(from Mielsen)
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

### [Function 5](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/the%205th%20function.py)：(from Mielsen)
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

### [Main function](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Tutorial%201/Main%20function.py)：(from Iassc)
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

## 5.[Compulsory Task 1](https://github.com/yung0705/ENG1003-T1_GP5/tree/main/Week%206%20Task/Task%201)
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
In this task, we also need to find out which type of model aircraft achieves the minimum flight cost. In the A-Star Path Planning Algorithm, there are 7 variables which will affect the total flight cost. They are "C_F", "Delta_F", "C_T", "Delta_T", "C_C", "Delta_F_A", "Delta_T_A". So, we need to change those variables to match the different aircraft models.
![圖片4](https://user-images.githubusercontent.com/89887457/141427285-9c36cb67-7024-411c-9985-be1984a62969.png)

##### [For PolyU-A380](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Task%201/Compulsory%20Task%201%20A380(minimum%20cost).py)
```
self.C_F = 1
self.Delta_F = 1
self.C_T = 2
self.Delta_T = 5
self.C_C = 10
        
self.Delta_F_A = 0.2
self.Delta_T_A = 0.2
```
##### [For PolyU-A381](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Task%201/Compulsory%20Task%201%20A381.py)
```
self.C_F = 1
self.Delta_F = 1.5
self.C_T = 3
self.Delta_T = 5
self.C_C = 10
        
self.Delta_F_A = 0.3
self.Delta_T_A = 0.4
```
##### [For PolyU-A382](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Task%201/Compulsory%20Task%201%20A382.py)
```
self.C_F = 1
self.Delta_F = 2
self.C_T = 4
self.Delta_T = 5
self.C_C = 10
        
self.Delta_F_A = 0.4
self.Delta_T_A = 0.5
```
##### [For PolyU-A383](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Task%201/Compulsory%20Task%201%20A383.py)
```
self.C_F = 1
self.Delta_F = 2.5
self.C_T = 5
self.Delta_T = 5
self.C_C = 10
        
self.Delta_F_A = 0.5
self.Delta_T_A = 0.1
```
### Result：
After we input the above value, we can get the total cost of among four different types of aircraft models:
PolyU-A380: Total flight cost = 3356.469824904021
![2021-11-12 (10)](https://user-images.githubusercontent.com/89887457/141428888-a08b0e68-a6a4-45f8-b95a-9d6097e79883.png)
PolyU-A381: Total flight cost = 4236.151346762756
![2021-11-12 (9)](https://user-images.githubusercontent.com/89887457/141428692-91fcc864-2dd5-4e57-908a-b8adbe00831d.png)
PolyU-A382: Total flight cost = 5115.8328686214945
![2021-11-12 (11)](https://user-images.githubusercontent.com/89887457/141429034-3bf58ebe-2a0f-46d9-9e9a-490863e65f4b.png)
PolyU-A383: Total flight cost = 5995.514390480228
![2021-11-12 (12)](https://user-images.githubusercontent.com/89887457/141429269-c2501679-610d-451d-aedd-ccd04942a9ed.png)

### Discussion：
We faced a problem that our program did not show the fuel consumption area, as we have inputted the data from the left upper corner (15,40) to the right bottom corner (30,20). However, In the language of python, it assumes that the user should put the data (coordinate) from lowest to highest (from left bottom to right upper). Therefore, we cannot get the predicted outcomes. We tried several times and figured out that the rules of entering data. So, we input (15,30) and (20,40) instead of (15,40) and (30,20). Then the area appeared.

## 6.[Compulsory Task 2.1](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Compulsory%20Task%202(2%20variables).py)
### Methodology：
The main goal for this task is to find the data about "Cf" and "Ct" to obtain the minimum cost for the PolyU-A380 aircraft model.

The constraints of the data are:

**Ct-Cf≤30**

**-0.5Ct-Cf≤-30**

**2Ct-Cf≥20**

**-4Ct-Cf≥-220**

So, using the Linear programming method, we can draw a graph and find the region that satisfies the condition. For the cost function, we can search for the appropriate "Ct" and "Cf" in the region to make the C minimize.
### Result：
After finishing the graph, we find that "Cf" must be 20 and "Ct" must be 20. In this condition, the minimum cost is 33602.88201522425
![2021-11-12 (13)](https://user-images.githubusercontent.com/89887457/141431633-0def44be-be20-479a-966c-c800ded781bb.png)

### Discussion：
After discussing this data, our group thinks it is actually the final goal.

## 7.[Compulsory Task 2.2](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Group5%20compulsory%20task%202%20aircraft%20models(4%20contriaints%20with%206%20variables).py)
### Methodology：
In this task, we should find six figures to find the minimum cost. The constraints of these data are shown below.

**Cf∆𝐹+Ct∆T≥25** 

**Cf+Ct≥10**

**∆𝐹+∆T≥10**

**∆𝐹a+∆𝑇a≥10**

**All variables>0,integer**

We can Combine this with **C=Cf*(∆𝐹+∆𝐹a)+Ct*(∆𝑇+∆𝑇a)+Cc**, then the final goal will be found.
### Result：
After analyzing these functions, we let **Cf=2, ∆𝐹=8, Ct=1, ∆𝑇=9, ∆𝐹a=1, ∆𝑇a=9**. In this condition, the minimum cost is 5602.601656214276
![2021-11-12 (15)](https://user-images.githubusercontent.com/89887457/141433475-4342e5b8-162e-4607-b855-eea36d4e9069.png)

### Discussion：
We think that this task is much more difficult than the task 2.1. So, we try more figures to satisfy these constraints. The method maybe not be serious, but we think these data maybe be the final goals.

## 8.[Compulsory Task 3](https://github.com/yung0705/ENG1003-T1_GP5/blob/main/Week%206%20Task/Compulsory%20Task%203%20.py)
### Methodology：
The goal of this task is to design a new cost area that can reduce the cost. Before adding code, I need to understand the original code. First, I need to set new attributes of AStarPlanner, which are minus_cost_x, minus_cost_y, C_P, and Delta_P. Then, I need to add ```+self.C_P*self.Delta_P``` to the cost-calculating equation for this new area.
![螢幕擷取畫面 2021-11-10 185614](https://user-images.githubusercontent.com/89887457/141402794-795b78c4-e84d-4518-b386-01362e1d1706.png)
![螢幕擷取畫面 2021-11-10 185839](https://user-images.githubusercontent.com/89887457/141421855-67f6957d-5a7a-46e2-865c-10691a52be3a.png)

Also, I need to change the motion model because more things need to be calculated. For the new situation, which is when the aircraft goes through the minus-cost area, I added
```
if self.calc_grid_position(node.x, self.min_x) in self.minus_cost_x:
	if self.calc_grid_position(node.y, self.min_y) in self.minus_cost_y:
		node.cost = node.cost - self.Delta_P * self.motion[i][2]
```
![螢幕擷取畫面 2021-11-10 190047](https://user-images.githubusercontent.com/89887457/141403233-0bbde9e6-9151-42b7-a782-7b4846a0cc20.png)

. That is all of the calculating part.
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
![1](https://user-images.githubusercontent.com/89887457/141421780-6e959457-9899-4a3d-bf8d-0709176124f7.png)
decreased to 2685.6271124294003
![2](https://user-images.githubusercontent.com/89887457/141421757-ab664984-c203-4b4e-825b-2f2a96cb5659.png)
![Figure 1 2021-11-12 16-57-09_1](https://user-images.githubusercontent.com/89887457/141441501-4b5d2388-6778-4257-8cff-c174a4ad86fb.gif)

### Discussion：
We think the difficult part of this task is that we need to read and understand the code. It is because this task is different from previous tasks. In this task, we are not only changing the numbers but also adding some new code. So understanding the code is necessary for preventing errors and incorrect outcomes. For example, in line 167, if I just follow the code from line 156 or 162, we can see that the path is evading the minus-cost area. This result does not make sense.
![螢幕擷取畫面 2021-11-12 112220](https://user-images.githubusercontent.com/89887457/141403676-8edd2584-f65b-45d3-a521-f9fc40ad03a9.png)

For the minimum cost, the aircraft should go through that area. After researching, I found that in line 167 the sign between "node.cost" and "self.Delta_P" should be "-"
```
node.cost = node.cost - self.Delta_P * self.motion[i][2]
```
. Then, the result will be correct

## 9.Reflective Essay
### CHENG Yung
In this freshman project, I have contributed to the main function in tutorial task and compulsory task 1. This gave me an opportunity to learn programing code and other soft skills like cooperating with teammates.

First and foremost, this project developed my adversity ability. When I faced error in running the code, I have to debug it by myself. As, there is not solution in the lecture material. Therefore, I have to find resources online by Google. I have also learnt to use a powerful resource called GitHub, which we can use other’s coding. In addition, In compulsory task 1 I found that python default input system is from small number to large number. However, the map from the lecture slides did not gave the from small coordinate to large coordinate. With this challenge, me and Mielsen try several times and have discovered that the input system of python is from left bottom to right top corner.

Second, I have also learnt programming language python in this project with the code editing tool Visual Studio Code. Although I still cannot fully understand the detail of a star program code, I can find it on GitHub and modify it. This problem-solving skill it more important instead. Moreover, I feel good when I work with my groupmate and finish the code. This is a bunch of sense of success when we get the correct outcome.

Finally, I feel grateful to have a chance to work with my classmate both from AAE department or EIE department.

### LI Mingjue 
In this assignment, I have done the research of the theory of path planning algorithm and the information about the uses of the python and GitHub. In addition, I also have cooperated with my teammate to calculate the data in the task 2.2.

 Firstly, it was easy for me to get the information about the introduction of the python and GitHub because I can search for many kinds of introductions on the Internet, such as from Google or Baidu. However, for the theory of path planning algorithm, it was hard to find very detailed information at first. Fortunately, I finally found a detailed introduction to the theory of path planning algorithm on a Chinese website. I sorted out some of the key information and wrote it in a word document.

 After that, I had a discuss with my teammate Man about the calculate about the task 2.2. Because, that is harder than the task 2.1, so we cooperated to deal with the task 2.2. Actually, we accidentally found the answer based on the rule of task 2.1 because it is too complicated to solve the functions in the task 2.2.
### MAN Yuanzhuo
In this task, I have finished the one which included two questions (2.1 & 2.2) with my groupmate Ethan. We used GitHub to find the requirement of the question. Then, we used VScode to try many data to seek for most appropriate answer. From these steps, we found a correct way to look for the final answer and we practiced how to calculate the data.
What is more, from this program, not only that we learned how to use the app such as VScode and GitHub, but we learnt that how to cooperate with my groupmates to find the answer together. Thanks to my groupmates. That is the most important way to solve this problem.

### LAW Wai Wah
In this freshman project, I contributed tutorial tasks and wrote the background of aeronautical engineering path planning. This gives me the opportunity to learn programming code and other soft skills, such as working with teammates.

First of all, this project has cultivated my ability to solve problems. When I encounter an error while writing code, I must find a way to find the omission. Because there is no solution in the handout. Therefore, I had to search for resources on the Internet through Google and ask the team members for help. I also learned to use a powerful resource called GitHub, where we can use other people's coding. In addition, when writing the background of path planning, I also understood the basic common sense and purpose of path planning. I also know that in today's aviation industry, it is used in major companies to reduce risks for carrying passengers.

Secondly, I also used the code editing tool Visual Studio Code in this project to learn the programming language python. Although I still cannot fully understand the details of a star program code, I can find and modify it on GitHub. This ability to solve problems is even more important. In addition, when I work with my teammates and finish the code, I understand the importance of teamwork. I received a lot of help from my team members and I am very grateful to them.

### LUK Man Chun
In this AAE freshman project, I have done functions 4 and 5 of the tutorial task, and compulsory task 3. In the past 11 weeks, I learned a lot.

First, I gained many chances to improve my programming skills. I learned a new programe language, Python, and software, Visual Studio Code. This is my first time using them. When I was doing the task, errors often came out. I need to check the code, again and again, to find out the problem and then debug it. Especially in compulsory task 3. I am not only changing the numbers but also adding some new code. Therefore understanding the code is necessary for preventing errors and incorrect outcomes. My logical thinking and problem-solving skills are enhanced after this project.

Second, I learned about how to use Github which is a platform containing various programming information. There are many useful codes and tutorials. For example, in this project, we need to use a  path planning algorithm called "a-star" which is designed by others on Github. All of our compulsory tasks are based on this algorithm. Also, Github is a good place for doing group work. It provides a place for us to manage all files and share work.

Finally, teamwork is also one of my gains. In this project, I work with students who come from different departments, such as AAE.

## 10.References
 - 石湖一叶, 路径规划基本理论, 2019. [Online]. Available:https://blog.csdn.net/CHN_ZHero/article/details/90286724 [Accessed: October 15, 2021]
