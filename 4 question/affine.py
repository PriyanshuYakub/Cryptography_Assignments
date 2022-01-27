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


def MultiEncryption(PlainText,Key):
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
    #print("for key = ", Key, "PLain text is : ",out.upper())
    return out.upper()


def AddEncryption(PlainText,Key):
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
    #print("for key = ", Key, "PLain text is : ",out.upper())
    return out.upper()



def Multiplicative_Decrypt(CT,k):
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


def Additive_decrypt(CT,k):
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



def AffineCipher(PlainText,k1,k2):
    T = MultiEncryption(PlainText,k1)
    CT = AddEncryption(T,k2)
    print("for Key Pair(",k1,", ",k2,") Ciphertext is : ",CT)
    return CT

#combination of additive and multiplicative decryptiom:
def AffineBruteForce(CT):
    print("\nBruteForcing AffineCipher for Cipher Text: ", CT)
    k = [1,3,5,7,9,11,15,17,19,21,23,25]
    for k1 in k:
        for k2 in range (1,27):
            P = Multiplicative_Decrypt(Additive_decrypt(CT,k2),k1)
            print("for Key Pair(",k1,", ",k2,") Plain Text is : ", P)


def main():
    PT = input("Input PlainText: ")
    #ensuring no spaces in given text
    PT = PT.replace(" ","")
    k1 = int(input("Input key 1 or multiplicative key: "))
    k2 = int(input("Input key 2 or Additive key: "))
    CT = AffineCipher(PT,k1,k2)
    AffineBruteForce(CT)

#calling main
main()