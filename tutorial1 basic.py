def function1():
    Name = ["Isaac", "Mielsen", "Ethan", "James", "MAN" ]
    print (*Name, sep = "\n")

def function2():
    a = 5
    b = 7
    c = 9
    print("a=",a , "b=",b ,"c=",c ,"sum=", (a+b+c))

def function3():
    a = 5
    print("a=",a , " Square of a:" , a**2)

def function4():
    (a,b)=(5,4)
    print("a=", a, "b=" , b)
    if a > b:
        print("a is larger than b")
    elif a > b:
        print("good")
    else:
        print("a=b")

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