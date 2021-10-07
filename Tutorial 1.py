def function1():
    print('This text represent the content of function 1')  #To be edited by member 1, Replace this line with your actual function code
    

def function2():
    print('This text represent the content of function 2')  #To be edited by member 2, Replace this line with your actual function code


def function3():
    a=5
    print("a=",a,"Square of a:", a**2)


def function4():
    x = int(input("Square Size:"))
    for num in range(x): 
        for num in range(x): 
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
