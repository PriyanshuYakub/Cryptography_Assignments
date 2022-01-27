#in one time pad encryption and decryption are done by same function
#we are using the ascii values to do encryptions and decryptions

import random
import string

def randKey(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))


def EncAndDec(text,Key):

	text = text.lower()
	#converting string to list
	text1 =[]
	text1[:0]=text
	key1 = []
	key1[:0] = Key
	T = []
	for (c,k) in zip(text1,key1):
		c_num = ord(c)
		k_num = ord(k)
		#using bitwise xor operator on each ascii value of text and key
		T.append(c_num^k_num)
	String_out = [chr(o) for o in T]
	out = ''.join(String_out)
	return out.upper()


def main():
	PT  = input("Input plain Text: ")
	PT = PT.replace(" ", "") #removing spaces in plain text
	Key = randKey(N = len(PT))
	print("Randomly generated Key: ", Key)
	CT = EncAndDec(PT,Key)
	print("\n Cipher Text:",CT)
	print("Decrypted Plain Text : ", EncAndDec(CT,Key).lower())

main()