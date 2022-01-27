#using simple euclidian algorithm to get GCD of two numbers
def getGCD(n,b):
	r1 =n
	r2 = b
	while(r2>0):
		q = int(r1/r2)
		r = r1-q*r2
		r1 = r2
		r2 = r
	return r1


#using extended euclidian algorithm to get inverse modulo
def getModInverse(n,b):
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

def main(x,y):
    n = int(x)
    b = int(y)

    gcd = getGCD(n,b)
    print("Gcd of given numbers is ", gcd)
    if gcd == 1:
        inv = getModInverse(n,b)
        print("inverse of " , b ,"in modulo ", n," is: ", inv)
    else:
        print("Gcd of given numbers is not equal to one so inverse doesn't exist")
    pass


x = input("Input n in modulo n: ")

y = input("input number to get GCD and modulo of: ")

main(x,y)