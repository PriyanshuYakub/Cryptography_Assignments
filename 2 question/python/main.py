#Euclidian algorithm to get GCD
def getGCD(b,n):
    r1 =n
    r2 = b
    while(r2>0):
        q = int(r1/r2)
        r = r1-q*r2
        r1 = r2
        r2 = r
    return r1


#usiing extended euclidian algorithm to get inverse modulo
def getModInverse(b,n):
    r1 =n
    r2 = b
    t1 = 0
    t2 = 1
    while(r2>0):
        q = int(r1/r2)
        r = r1-q*r2
        r1 = r2
        r2 = r
        #inverse part
        t = t1- q*t2
        t1 = t2
        t2 = t
    #to maintain +ve inverse value and that it is in Zn 
    if(t1<0):
        t1 = n +t1
    return t1

#getting additive inverse
def getAddInv(a,n):
    return n-(a%n)


#addition in modulo n
def add():
    print("\nAddition: (a+b) modulo n")
    n = int(input("Enter Value of 'n': " ))
    a = int(input("Enter Value of 'a': " ))
    b = int(input("Enter Value of 'b': " ))

    s = (a+b)%n
    print("(",a,"+",b,")modulo",n," = ",s)

#subtraction in modulo n
def diff():
    print("\nSubtraction: (a-b) modulo n")
    n = int(input("Enter Value of 'n': " ))
    a = int(input("Enter Value of 'a': " ))
    b = int(input("Enter Value of 'b': " ))

    d = (a-b)%n
    print("(",a,"-",b,")modulo",n," = ",d)


#multiplication in modulo n
def multi():
    print("\nMultipliacation: (a*b) modulo n")
    n = int(input("Enter Value of 'n': " ))
    a = int(input("Enter Value of 'a': " ))
    b = int(input("Enter Value of 'b': " ))

    m = (a*b)%n
    print("(",a,"*",b,")modulo",n," = ",m)


#Division in modulo n
def division():
    print("\nDivision: (a/b) modulo n NOTE:only possible if b has multiplicative inverse in modulo n")
    n = int(input("Enter Value of 'n': " ))
    a = int(input("Enter Value of 'a': " ))
    b = int(input("Enter Value of 'b': " ))

    #check wether b has multiplicative inverse or not if not division is not possible
    #(b * q) % n = a % n. concept we find c as inv(b)*a%n = q
    if (getGCD(b,n) == 1):
        inverse = getModInverse(b,n)
        q = (inverse*a)%n
        print("(",a,"/",b,")modulo",n," = ",q)
    else:
        print("Inverse of",b," in modulo ",n, " Doesn't exist, therefore:\n Division not Defined")


def aInv():
    print("\nAdditive inverse: a + x ≡ 0 modulo n, we need x")
    n = int(input("Enter Value of 'n': " ))
    a = int(input("Enter Value of 'a': " ))
    print("Additive inverse of ",a,"modulo",n," = ", getAddInv(a,n))

def mInv():
    print("\nMultiplicative inverse: a * x ≡ 1 modulo n, we need x")
    n = int(input("Enter Value of 'n': " ))
    a = int(input("Enter Value of 'a': " ))
    if(getGCD(a,n)==1):
        print("Multiplicative inverse of ",a,"modulo",n," = ", getModInverse(a,n))
    else:
        print("inverse Doesn't exist as GCD of",a," and ",n,"is not equal to 1" )

#main menu definition
def menu():
    
    print("\nWhat would you like to do?")
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Additive Inverse \n6.Multiplicative Inverse")
    print("7.Quit")
    
    #using python dictionary to create switcher case and call respective functions
    case = {
            "1":add,
            "2":diff,
            "3":multi,
            "4":division,
            "5":aInv,
            "6":mInv,
            }
    #input        
    option = input("Select your option: ")
    if(option=="7"):
        print("\nThank you for using MODULAR ARITHMETIC CALCULATOR\n By: Priyanhsu Yakub 20BCE7305")
        return True
    else:
        case[option]()
        return False

#looping the menu till exit is pressed        
exit = False;
print("\n-----MODULAR ARITHMETIC CALCULATOR--------By: Priyanhsu Yakub 20BCE7305-----------")
while (exit==False):
    exit = menu()
