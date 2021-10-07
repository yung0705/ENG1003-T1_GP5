
def MemberName():
    Name = ["Isaac", "Mielsen", "Ethan", "James", "MAN" ]
    print (*Name, sep = "\n")

def Line():
    a = 5
    b = 7
    c = 9
    print("a=",a , "b=",b ,"c=",c ,"sum=", (a+b+c))

def Lok():
    a = 5
    print("a=",a , " Square of a:" , a**2)



def Q4():
    (a,b)=(5,4)
    print("a=", a, "b=" , b)
    if a > b:
        print("a is larger than b")

    
x = int(input("Enter the function Number to be executed(1-4):"))
if (x==1):
    MemberName()
elif (x==2):
    Line()
elif (x==3):
    Lok()
elif (x==4):
    Q4()
else:
    print("please enter(1-4)")
    