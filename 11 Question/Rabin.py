import random
import math

#gcd to check if given Plain text is valid
def getGCD(n,b):
    r1 =n
    r2 = b
    while(r2>0):
        q = int(r1/r2)
        r = r1-q*r2
        r1 = r2
        r2 = r
    return r1


def Divisibility_test(n):
    r = 2
    while(r< math.sqrt(n)):
        if(n%r==0):
            return False
        r += 1
    return True


#mersenne
def PrimeGen():
    # can use mersenne primes too
    prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    while True:
        p = prime_list[random.randint(1,len(prime_list)-1)]
        Mi = pow(2,p)-1
        if(Divisibility_test(Mi)):
            return Mi
    # while True:
    #     n = random.randint(1,100)
    #     fn = 2*n + 3
    #     gn = n**2 + 1
    #     hn  = 2**n + 1
    #     if(Divisibility_test(hn)):
    #         return hn
    #     elif(Divisibility_test(gn)):
    #         return gn
    #     elif(Divisibility_test(fn)):
    #         return fn
    #     else:
    #         print("prime not found repeat loop")


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


#modified CRT for Rabin system which has only two equations
def crt(a,b,p,q):
    #initialising M
    M = p*q
    M1 = M/p
    M2 = M/q

    inv_M1 = getModInverse(p,M1)
    inv_M2 = getModInverse(q,M2)
    x = (a*M1*inv_M1 + b*M2*inv_M2)%M       

    return int(x) #not necessary but just to remove decimal point which occurs as we used multiplication

#check prime if of fprm 4k + 3
def prime_check(n):
    if (n-3)%4 == 0:      
        return True
    return False



def Rabin_KeyGen():
    while True:
        p = PrimeGen()
        if prime_check(p):
            break
        
    while True:
        q = PrimeGen() #use generator here
        if prime_check(q) and p!=q:
            break    
    
    n = p*q

    Public_key = n
    Private_key = (p,q)

    return (Public_key, Private_key)




def Rabin_Encryption(n,P): #n is public key P is from Zn*
    C = pow(P,2)%n
    return C




def Rabin_Decryption(p,q,C):
    a1 = (C**((p+1)//4))%p
    a2 = (-(C**((p+1)//4)))%p
    b1 = (C**((q+1)//4))%q
    b2 = (-(C**((q+1)//4)))%q
    #using crt:
    P1 = crt(a1,b1,p,q)
    P2 = crt(a1,b2,p,q)
    P3 = crt(a2,b1,p,q)
    P4 = crt(a2,b2,p,q)
    return (P1,P2,P3,P4)


Keys = Rabin_KeyGen()
Public_key = Keys[0]
Private_key = Keys[1]
print("Public Key generated: n = ",Public_key)
print("Private keys generated: p = ",Private_key[0], " q = ",Private_key[1])
#encryption call by alice
while True:
    PT  = int(input("Input Plaintext which is a part of Zn* where n is the public key given:  "))
    if getGCD(Public_key,PT) == 1:
        break
    else:
        print("Invalid input, please try again")

CT = Rabin_Encryption(Public_key,PT)
print("Ciphert text: ",CT)

#decryption call
p = Private_key[0]
q = Private_key[1]
print("Decryption of Ciphertext generates 4 different text and the plain text is one of them:\n ",Rabin_Decryption(p,q,CT))

