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
#The Main function edited by Group leader
print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

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
