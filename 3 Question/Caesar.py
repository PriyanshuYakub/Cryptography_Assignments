

 #casesar cipher or simply Additive cipher
def Encryption(PlainText, Key):
	#ensuring uniformity of plaintext using lower() function	
	PlainText = PlainText.lower()
	PTno = []
	#converting plain text to numbers
	for character in PlainText:
		number = ord(character)-97
		PTno.append(number)
	#checking if given key is valid
	exists = False
	for k in range (1,27):
		if Key == k:
			exists = True
	if exists == False:
		print("given key is not valid")
		return False
	#creating output
	output = []
	for j in PTno:
		num = (j+Key)%26 +97
		output.append(num)
	#converting from number to letters
	string_out = [chr(o) for o in output]
	out = ''.join(string_out)
	print("for key = ", Key, "Cipher text is : ",out.upper())
	return out.upper()


def Decrypt(CT,k):
    CT = CT.lower()
    CTno = []
    for character in CT:
        number = ord(character) - 97
        CTno.append(number)
    output = []
    for i in CTno:
        num = (i-k)%26 +97
        output.append(num)
    string_out = [chr(o) for o in output]
    return ''.join(string_out)



def BruteForce(CT):
    print("\nBruteForcing Xaesar Cipher for Cipher Text: ", CT)
    for k in range (1,27):
    	P = Decrypt(CT,k)
    	print("for Key = ",k,", Plain Text is : ", P, )


PT = input("Input PlainText: ")
#ensuring no spaces in given text
PT = PT.replace(" ","")
k = int(input("Input key: "))

e = Encryption(PT,k)
if e != False:
	#BruteForceCaesar(e)
	BruteForce(e)
