def Encryption(PlainText,k):
    #removing blank spaces in given string
    PT = PlainText.replace(" ","")
    #converting plain text to numbers
    PT = PT.lower()
    
    PTno = []
    Key = []
    Key.append(k)
    #adding all charcter numbers to Plaintext and key list
    for char in PT:
        num = ord(char) - 97
        PTno.append(num)
        Key.append(num)
    #removing last element from list as it is not needed
    Key.pop()
    CTno = []
    for(pi,ki)in zip(PTno,Key):
        CTno.append((pi + ki)%26 + 97)

    CT_out = [chr(o) for o in CTno]
    CT =''.join(CT_out)
    return CT.upper()



def Decryption(CT,key):
    #once we decrypt the first letter we have to use the same letter to decrypt next letter
    CT = CT.lower()
    CTno = []
    for char in CT:
        num = ord(char) - 97
        CTno.append(num)
    ki = key
    
    P = []
    for c in CTno:
        P.append((c-ki)%26 +97)
        ki = (c-ki)%26
    PT_out = [chr(o) for o in P]
    PT = ''.join(PT_out)
    return PT

def main():
    PT = input("Enter Text: ")
    PT = PT.replace(" ", "") #removing spaces in plain text
    Key = int(input("Input key in range 0-25: "))
    CT = Encryption(PT,12)
    print("Encrypted message: ",CT)
    print("\n Decryting message gives: ",Decryption(CT,12))

main()
