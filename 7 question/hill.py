import numpy as np
import math
#get inverse modulo n of a number b
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


def Encrypt(p,k):
	#matrix multiplication:
	out = p@k
	out %= 26
	return out


def Decrypt(CT,K):
	D = round(np.linalg.det(K))
	D_inv = getModInverse(26,D%26)

	#as inverse of matrix is adj/det => inv*det = adj
	Adj_K = np.linalg.inv(K)*np.linalg.det(K)
	#using round because linalg library uses linear algebra and doesn't give exact integer output but a very close decimal value
	Adj_K = np.round(Adj_K)
	Adj_K = Adj_K.astype(int)
	Adj_K %=  26

	K_inv = D_inv*Adj_K
	K_inv %=26
	out = CT@K_inv
	out %= 26

	return out


#decoding function to decode cipher text
def decoding(matrix,n):
	out = []
	for m in matrix:
		for i in m:
			out.append(chr(i+97))
	return ''.join(out)


def main():
	#note the matrix condition must be met 
	#if the number of elements is less than that required dummy variables will be introduced
	#dummy char will be Z i.e., its value 25
	#if number of elements is greater than necessary matrix will need to be redefined 
	#therefore must reneter key
	n = int(input("The Key matrix is a square matrix input n for nxn matrix: "))
	PT = input("Enter plain text: ")
	PT = PT.replace(" ", "") #removing spaces in plain text
	while(True):
		Key = input("Enter key string: ")
		Key = Key.lower()
		if(n**2<len(Key)):
			print("Key size is more than matrix re-enter key \n")
		else:
			break
	#converting key to list of required numbers:
	Kno = []
	#converting plain text to numbers
	for character in Key:
		number = ord(character)-97
		Kno.append(number)
	#adding dummy characters
	if(len(Kno)<n**2):
		m = len(Kno)
		for i in range(0,n**2-m):
			Kno.append(25)
	
	temp = []
	matrix_k = []
	j = 0
	for i in Kno:
		temp.append(i)
		j +=1
		if j % n == 0:
			matrix_k.append(temp)
			temp = []
			j = 0
	
	
	# plaintext matrix can only have n columns
	#for plain text conver it to a list append required dummy variables
	#for char in list, inner loof for i in n
	PT = PT.lower()
	PTno = []
	#converting plain text to numbers
	for character in PT:
		number = ord(character)-97
		PTno.append(number)
	if(len(PTno)%n!=0):
		m = len(PTno)%n
		for i in range(0,n-m):
			PTno.append(25)
	print("PlainText in encoded into numbers: ",PTno)
	print("Key in encoded into numbers: ",Kno)
	temp = []
	matrix_PT = []
	j = 0
	for i in PTno:
		temp.append(i)
		j +=1
		if j % n == 0:
			matrix_PT.append(temp)
			temp = []
			j = 0
	
	
	k = np.array(matrix_k)
	p = np.array(matrix_PT)

	#determinant
	D = round(np.linalg.det(k))%26
	if(math.gcd(D,26)==1):
		CT = Encrypt(p,k)
		print("Cipher text: ",CT," ==> ",decoding(CT,n).upper())
		t = Decrypt(CT,k)
	#converting cipher text to letters
		print("Decrypted output",t,"==>",decoding(t,n))

	else:
		print("Given key's determinant doen't have multiplicative inverse in Zn26")
	
	

main() 

