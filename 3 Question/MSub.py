
#usiing extended euclidian algorithm to get inverse modulo
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


#multiplicative encryption using given plain text
def Encryption(PlainText, Key):
	#ensuring uniformity of plaintext using lower() function	
	PlainText = PlainText.lower()
	PTno = []
	#converting plain text to numbers
	for character in PlainText:
		number = ord(character)-97
		PTno.append(number)
	#all possible multiplicative keys i.e. Zn*
	keys = [1,3,5,7,9,11,15,17,19,21,23,25]
	#checking if given key is valid
	exists = False
	for k in keys:
		if Key == k:
			exists = True
	if exists == False:
		print("given key is not valid")
		return False

	#creating output
	output = []
	for j in PTno:
		num = (j*Key)%26 +97
		output.append(num)
	string_out = [chr(o) for o in output]
	out = ''.join(string_out)
	print("for key = ", Key, "Cipher text is : ",out.upper())
	return out.upper()

def Decrypt(CT,k):
    k_inv = getModInverse(26,k)
    CT = CT.lower()
    CTno = []
    for character in CT:
        number = ord(character) - 97
        CTno.append(number)
    output = []
    for i in CTno:
        num = (i*k_inv)%26 +97
        output.append(num)
    string_out = [chr(o) for o in output]
    return ''.join(string_out)


def BruteForce(CT):
    print("\nBruteForcing Multiplicative Substitution for Cipher Text: ", CT)
    keys = [1,3,5,7,9,11,15,17,19,21,23,25]
    for k in keys:
    	P = Decrypt(CT,k)
    	k_inv = getModInverse(26,k)
    	print("for Key = ",k,",i.e., k^-1(inverse key) = ",k_inv,", Plain Text is : ", P, )

# def BruteForceMsub(CT):
# 	#turning cipher text into numbers:
# 	print("\n Brute forcing given Ciphertext: ",CT)
# 	CT = CT.lower()
# 	CTno = []
# 	for character in CT:
# 		number = ord(character) - 97
# 		CTno.append(number)
# 	k = [1,3,5,7,9,11,15,17,19,21,23,25]
# 	output = []
# 	for i in k:
# 		for j in CTno:
# 			num = (j*i)%26 +97
# 			output.append(num)
# 			string_out = [chr(o) for o in output]
# 		print("for k-1 (inverse of key)= ", i, "PLain text is : ",''.join(string_out))
# 		output = []


PT = input("Input PlainText: ")
#ensuring no spaces in given text
PT = PT.replace(" ","")
k = int(input("Input key: "))

e = Encryption(PT,k)
if e != False:
	#BruteForceMsub(e)
	BruteForce(e)