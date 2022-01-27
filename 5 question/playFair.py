#note dummy variable is X
import string


# create matrix without duplicates

#find index of given element in matrix as i,j
def get_index(matrix, element):
	for i in matrix:
		if element == 'I':
			element = ('I','J')

		if element == 'J':
			element = ('I','J')
		if(element in i):
			return (matrix.index(i),i.index(element))


def k_exists(matrix, k):
	#here i is each sub list which as a whole form the matrix
	for i in matrix: 
		exists = k in i
		if(exists):
			return True
	return False


def handle_IJ(matrix): #for handling I,j
#iterating throught each sub list to 
#find existence of I as we only allowe I to be entered
	for i in matrix: 
		exists = 'I' in i
		if(exists):
			matrix[matrix.index(i)][i.index('I')] = ('I','J')
	return matrix
	# return False


def key_matrix(Key): #key is a string
	Key = Key.upper()
	#initialising matrix with dummy values to be edited later when filling
	K_matrix = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]
	i = 0
	j = 0
	for k in Key:
		if(k_exists(K_matrix,k)!= True):
			if k == 'J': #replacing J with I it will be replaced later with (I,J)
				k = 'I'
			K_matrix[i][j] = k
			j +=1
		if(j>=5): #resetting value of j to go to next row
			j = 0
			i +=1
	#getting string of alphabets to enter
	alphabet_string = string.ascii_uppercase
	allowed_alphabet = []
	for char in alphabet_string:
		if(k_exists(K_matrix,char)!= True):
			if char != 'J':
				allowed_alphabet.append(char)		
	for c in allowed_alphabet:
		K_matrix[i][j] = c
		j+=1
		if j>=5:
			j =0
			i +=1
	# print(K_matrix)
	final_key_matrix = handle_IJ(K_matrix)


	# print(final_key_matrix)
	return final_key_matrix


#creating pairs  using list and 
#tuples we use tuple as it is ordered and unchangable
def get_pairs(PlainText): #creating letter pairs of given plain text
	PlainText = PlainText.lower()
	string_len = len(PlainText)
	#gonna take values and then we convert to tuple when pair filled
	temp = [] 
	i = 0
	j = 0
	pair_list = []
	for char in PlainText:
		if(char in temp): #checking possibility of duplicate in pai
			temp.append('x')
			pair_list.append(tuple(temp))
			i = 0
			temp = []
		temp.append(char)
		i += 1
		if i == 2:
			i = 0
			pair_list.append(tuple(temp))
			temp = [] #resetting
	#if last pair not made 
	if temp != []:
		temp.append('x') #dummy val
		pair_list.append(tuple(temp))
	

	return pair_list




def Encrypt_pair(pair, key_matrix):
	a = pair[0].upper()
	b = pair[1].upper()
	i1 = get_index(key_matrix,a)
	i2 = get_index(key_matrix,b)


	#if in same row
	if(i1[0] == i2[0]):
		if i1[1] >= 4:
			a_out = key_matrix[i1[0]][0]
		else:
			a_out = key_matrix[i1[0]][i1[1]+1]
		if i2[1] >= 4:
			b_out = key_matrix[i2[0]][0]
		else:
			b_out = key_matrix[i2[0]][i2[1]+1]
	
	#if in same column
	elif(i1[1] == i2[1]):
		if i1[0] >= 4:
			a_out = key_matrix[0][i1[1]]
		else:
			a_out = key_matrix[i1[0]+1][i1[1]]
		if i2[0] >= 4:
			b_out = key_matrix[0][i2[1]]
		else:
			b_out = key_matrix[i2[0]+1][i2[1]]
	

	#otherwise
	else:
		a_out = key_matrix[i1[0]][i2[1]]
		b_out = key_matrix[i2[0]][i1[1]]
	return (a_out,b_out)


def Decrypt_pair(pair, key_matrix):
	a = pair[0].upper()
	b = pair[1].upper()
	i1 = get_index(key_matrix,a)
	i2 = get_index(key_matrix,b)


	#if in same row
	if(i1[0] == i2[0]):
		if i1[1] <= 0:
			a_out = key_matrix[i1[0]][4]
		else:
			a_out = key_matrix[i1[0]][i1[1]-1]
		if i2[1] <= 0:
			b_out = key_matrix[i2[0]][4]
		else:
			b_out = key_matrix[i2[0]][i2[1]-1]
	
	#if in same column
	elif(i1[1] == i2[1]):
		if i1[0] <= 0:
			a_out = key_matrix[4][i1[1]]
		else:
			a_out = key_matrix[i1[0]-1][i1[1]]
		if i2[0] <= 0:
			b_out = key_matrix[4][i2[1]]
		else:
			b_out = key_matrix[i2[0]-1][i2[1]]
	

	#otherwise
	else:
		a_out = key_matrix[i1[0]][i2[1]]
		b_out = key_matrix[i2[0]][i1[1]]
	return (a_out,b_out)


def Encryption(PlainText,key):
	pair_list = get_pairs(PlainText)
	key_m = key_matrix(key)
	C_pair_list = []
	for pair in pair_list:
		c = Encrypt_pair(pair,key_m)
		C_pair_list.append(c)
	CT_list = []
	for pair in C_pair_list:
		for element in pair:
			if element == ('I','J'):
				CT_list.append('I')
			else:
				CT_list.append(element)
	CipherText = ''.join(CT_list)
	return CipherText


def Decryption(CipherText,key):
	pair_list = get_pairs(CipherText)
	key_m = key_matrix(key)
	P_pair_list = []
	for pair in pair_list:
		p = Decrypt_pair(pair,key_m)
		P_pair_list.append(p)
	PT_list = []
	for pair in P_pair_list:
		for element in pair:
			if(element != 'X'):
				if element == ('I','J'):
					PT_list.append('I')
				else:
					PT_list.append(element)
	PlainText = ''.join(PT_list)
	return PlainText.lower()



def main():
	PT  = input("Input plain Text: ")
	Key = input ("Input Key: ")

	PT = PT.replace(" ", "") #removing spaces in plain text

	CT  = Encryption(PT,Key)
	print("Cipher text is: ", CT, "\n")

	print("Decryption of above given ciphertext: ",Decryption(CT,Key))

main()
