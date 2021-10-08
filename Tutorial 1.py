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
else:
    print('There is no function. Please enter(1-4)')
