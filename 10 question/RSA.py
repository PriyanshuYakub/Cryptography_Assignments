
import random
import math

def Divisibility_test(n):
    r = 2
    while(r<=math.sqrt(n)):
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

def getGCD(n,b):
	r1 =n
	r2 = b
	while(r2>0):
		q = int(r1/r2)
		r = r1-q*r2
		r1 = r2
		r2 = r
	return r1
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
# #test :
# n = 159197
# totient_n = totient(n)
# print(totient_n)
#print(random.randrange(100, 1000, 3))

def RSA_KeyGen():
	#add generating function for p and q
	p = PrimeGen()
	while(True):
		q = PrimeGen()
		if p!=q :
			break
	#make sure p!=q
	print(p," ",q)
	n = p*q
	#as both are primes the value of totient(n) is given by this equation
	totient_n = (p-1)*(q-1) 
	
	cond = True
	while(cond):
		e = random.randrange(1, totient_n)
		if(getGCD(totient_n,e)==1):
			cond = False
	
	d = getModInverse(totient_n,e)

	Public_Key = (e,n)
	Private_key = d
	return (Public_Key,Private_key)

def RSA_encryption(P,e,n):
	C = pow(P,e)%n
	return C
def RSA_Decryption(C,d,n):
	P = pow(C,d)%n
	return P

def main():
	key_pair = RSA_KeyGen()
	Public_Key = key_pair[0]
	Private_key = key_pair[1]
	print("Public Keys generated: Public key e = ",Public_Key[0]," Public_Key n = ", Public_Key[1])
	print("Private key generated: Private key d = ",Private_key)
	P = int(input("Enter Plain text in Zn : "))
	C = RSA_encryption(P,Public_Key[0],Public_Key[1])
	print("RSA encrypted Cipher text: ",C,"\n")
	print("RSA Decrypted Plain text: ", RSA_Decryption(C,Private_key,Public_Key[1]))

main()