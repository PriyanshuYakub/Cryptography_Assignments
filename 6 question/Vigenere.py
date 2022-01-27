import math
import itertools
import string
import time

def Encryption(PlainText, Key):
    #convert plaintext and key into list of numbers
    #ensuring no spaces in given text
    PlainText = PlainText.replace(" ","")

    PlainText = PlainText.lower()
    PTno = []
    #converting plain text to numbers
    for character in PlainText:
        number = ord(character)-97
        PTno.append(number)

    Key = Key.lower()
    Kno = []
    #converting Key stream to numbers
    for character in Key:
        number = ord(character)-97
        Kno.append(number)


    #we will use this with mod and iterator and add to plain text no
    Kno_len = len(Kno) 
    k_iterator = 0
    
    output = []
    for i in PTno:
        num = (i+Kno[k_iterator%Kno_len])%26 +97
        output.append(num)
        k_iterator += 1
    string_out = [chr(o) for o in output]
    CT = ''.join(string_out)

    return CT.upper()

def Decryption(CipherText, Key):
    #convert plaintext and key into list of numbers
    
    CT = CipherText.lower()
    CTno = []
    #converting plain text to numbers
    for character in CT:
        number = ord(character)-97
        CTno.append(number)

    Key = Key.lower()
    Kno = []
    #converting Key stream to numbers
    for character in Key:
        number = ord(character)-97
        Kno.append(number)
   
    #we will use this with mod and iterator and add to plain text no
    Kno_len = len(Kno) 
    k_iterator = 0
    
    output = []
    for i in CTno:
        num = (i-Kno[k_iterator%Kno_len])%26 +97
        output.append(num)
        k_iterator += 1
    string_out = [chr(o) for o in output]
    PT = ''.join(string_out)

    return PT

#cryptanalysis
def Kasiski_test(CT):

    print("\n PERFORMING KASISKI TEST")
    #converting Ciphertext into list as list is easy to iterate through
    CT_list = []
    for char in CT:
        CT_list.append(char)
    CT_len = len(CT)
    Difference_list = [] #need to get gcd of numbers in this lis
    
    for i in range(0,CT_len):
       
        for j in range(i+5,CT_len):
            if(CT_list[i]==CT_list[j-2] and CT_list[i+1]==CT_list[j-1] and CT_list[i+2]==CT_list[j]):
                first_index = i
                second_index = j-2
                Difference = j-2-i
                Difference_list.append(Difference)
                break
    GCD = Difference_list[0]
    for i in range (1,len(Difference_list)):
        GCD = math.gcd(GCD,Difference_list[i])
    print("Key Length is multiple of: ", GCD)
    m = GCD
    #now we brute force using this information:
    #for experiment sake we will limit to m letter words 
    #storgae can go upto 100 mb so here we only go till code    
    for key_tuple in itertools.product(string.ascii_lowercase, repeat=m):
        key = ''.join(key_tuple)
        print("With Key = ",key," Decrypted message: ", Decryption(CT,key))
        


def main():
    #hard coding input for example can change key and plaintext
    #as per requirements.
    PT = "she is listening"
    K = "PASCAL"
    print("Given Plain text: ", PT)
    print("Given Key: ", K)
    CT = Encryption(PT,K)
    print("Cipher text when Encrypted: ", CT)
    print("Decryption of Cipher text: ",Decryption(CT,K))
    CT_test = "LIOMWGFEGGDVWGHHCQUCRHRWAGWIOWQLKGZETKKMEVLWPCZVGTHVTSGXQOVGCSVETQLTJSUMVWVEUVLXEWSLGFZMVVWLGYHCUSWXQHKVGSHEEVFLCFDGVSUMPHKIRZDMPHHBVWVWJWIXGFWLTSHGJOUEEHHVUCFVGOWICQLTJSUXGLW"
    print("\n sample cipher text for using kasiskit on: ", CT_test)
    time.sleep(5)
    Kasiski_test(CT_test)

main()



    
