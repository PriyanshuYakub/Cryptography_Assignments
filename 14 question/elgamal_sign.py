import random
import math
from math import gcd

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


def Divisibility_test(n):
    r = 2
    while(r< math.sqrt(n)):
        if(n%r==0):
            return False
        r += 1
    return True

#Fermats prime gen and other functiones mixed
def PrimeGen():
	while True:
		n = random.randint(1,100)
		fn = 2*n + 3
		gn = n**2 + 1
		hn  = 2**n + 1
		if(Divisibility_test(hn)):
			return hn
		elif(Divisibility_test(gn)):
			return gn
		elif(Divisibility_test(fn)):
			return fn
		else:
			print("prime not found repeat loop")


def primRoots(modulo):
    required_set = {num for num in range(1, modulo) if gcd(num, modulo) }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

def Elgamal_KeyGen():
	p = PrimeGen() #use generator here

	prim_root_list = []
	while(True):
		prim_root_list = primRoots(p)
		if prim_root_list != [] :
			break
		else:
			p = PrimeGen()
	
	#any number from 1 to p-2 as in Zp* all values from 1 to p-1 are present and it is a cyclic group
	d = random.randint(1,p-2) 
	e1 = random.choice(prim_root_list)
	e2 = (e1**d)%p

	PublicKey = (e1,e2,p)
	PrivateKey = d

	return (PublicKey,PrivateKey)

def Elgamal_Signature(e1,p,d,M):
	#as Zp* forms a group by itself excluding p :
	#we can choose a random integer(secret) from zp*
	while(True):
		r = random.randint(1,p-1)
		if(math.gcd(r,p-1)==1):
			break
	#r = 107 #used for testing
	#print("r = ", r)
	S1 = (e1**r)%p
	r1 = getModInverse(p-1,r)
	temp = (M-(d*S1))%(p-1)
	S2 = ((M-(d*S1))*r1)%(p-1)

	return (S1,S2)

def Elgamal_Verifiying(S1,S2,M,e1,e2,p):
	V1 = (pow(e2,S1)*pow(S1,S2))%p
	V2 = (e1**M)%p
	if(V1 == V2):
		return " Verified"
	return "Not Verified"

def main():
	key = Elgamal_KeyGen()
	PublicKey = key[0]
	PrivateKey = key[1]
	print("Sender:")
	print("Public keys generated e1,e2,p are : ", PublicKey)
	print("Private key generated d: ", PrivateKey)
	M = int(input("Input Message: "))
	e1 = PublicKey[0]
	e2 = PublicKey[1]
	p = PublicKey[2]
	print("\nReciever:")
	S = Elgamal_Signature(e1,p,PrivateKey,M)
	print("Signatures and Message:  ",S,",  ", M)
	print("Verification: ", Elgamal_Verifiying(S[0],S[1],M,e1,e2,p))

main()

