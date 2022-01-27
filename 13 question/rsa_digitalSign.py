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

#Signing
def Private_key_encryption(M,d,n):
	#S is signature
	S = pow(M,d)%n
	return S



def Signature_Decryption(S,e,n):
	M = pow(S,e)%n
	return M

#verifying
def Signature_confirmation(M1,M2):
	if M1 == M2:
		return True
	else:
		return False




def RSA_KeyGen():
	#add generating function for p and q
	p = PrimeGen()
	while(True):
		q = PrimeGen()
		#make sure p!=q
		if p!=q :
			break
	n = p*q
	#as both are primes the value of totient(n) is given by this equation
	totient_n = (p-1)*(q-1) 
	
	cond = True
	while(cond):
		e = random.randrange(2, totient_n-1)
		if math.gcd(e,totient_n)==1:
			cond = False
	
	d = getModInverse(totient_n,e)

	Public_Key = (e,n)
	Private_key = d
	return (Public_Key,Private_key)



def main():
	print("Sender: ")
	#key generation
	key_pair = RSA_KeyGen()
	Public_Key = key_pair[0]
	Private_key = key_pair[1]
	print("\nPublic key e = ",Public_Key[0]," Public_Key n = ", Public_Key[1])
	print("Private key generated: Private key d = ",Private_key)
	
	M = int(input("Enter Message in Zn : "))

	#Signing
	S = Private_key_encryption(M,Private_key,Public_Key[1])

	print("\nRSA Private key encrypted Signature is: ",S)
	print("message transmitted: ", (M,S))
	
	print("\nReciever: ")
	print("message recieved: ", (M,S))
	#verification
	M1 = Signature_Decryption(S,Public_Key[0],Public_Key[1])
	print("\nDecrypting Signature with public key gives: ", M1)
	if Signature_confirmation(M,M1):
		print("Given Message and Message decryped from signature are same Digital signature,origin verified, message not tampered with\n Message ACCEPTED")
	else:
		print("as signature is not giving original message when decrypted, user unverified\n Message Rejected")


main()