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
	
	d = random.randint(1,p-2) #any number from 1 to p-2 as in Zp* all values from 1 to p-1 are present and it is a cyclic group

	e1 = random.choice(prim_root_list)
	
	e2 = pow(e1,d)%p

	PublicKey = (e1,e2,p)
	PrivateKey = d

	return (PublicKey,PrivateKey)

def Elgamal_Encryption(e1,e2,p,P):
	#as Zp* forms a group by itself excluding p :
	#we can choose a random integer from zp*
	r = random.randint(1,p-1)
	print("random number chosen, r = ", r)
	C1 = pow(e1,r)%p
	C2 = (P*pow(e2,r))%p

	return (C1,C2)

def Elgamal_DEcryption(d,p,C1,C2):
	P = (C2*(getModInverse(p,pow(C1,d)%p)))%p
	return P

def main():
	key = Elgamal_KeyGen()
	PublicKey = key[0]
	PrivateKey = key[1]
	print("Public keys e1,e2,p are : ", PublicKey)
	print("Private key d: ", PrivateKey)
	P = int(input("Input Plain Text: "))
	e1 = PublicKey[0]
	e2 = PublicKey[1]
	p = PublicKey[2]
	CT = Elgamal_Encryption(e1,e2,p,P)
	print("Encrypted Message(Cipher text):  ",CT)
	print("Decrypted Message: ", Elgamal_DEcryption(PrivateKey,p,CT[0],CT[1]))

main()
