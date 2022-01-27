
#brute forcing to get k, generallly higher the k value more is the acurracy 
#so we find the highest value possible    

def get_mk(n):
    m = 1      
    k = 1
    while (n-1)%2**k ==0 :
        m = (n-1)/pow(2,k)
        k += 1
    return (int(m),int(k-1)) 
#k-1 because there will be an extra increment from above loop 
#also because we used multiplication 
#and division operaton they are floats so we convert to int



def Miller_Rabin(n,a=2): #for prime test base is generally 2
    mk = get_mk(n)
    #opening tuple to get m and k
    m = mk[0]
    k = mk[1]
    T = pow(a,m)%n #a^m mod n
    #print(T) used for debugging
    if T == +1%n | T== -1%n :
        return "A Prime"
    for i in range (1,k):
        T = pow(T,2)%n
        #print(i,T,n) used for debugging
        #we are using (+ or -)1%n because inherently python 
        #doesn't know if given number is equal to -1
        if T == 1%n: #is T = 1 mod n
            return "A Composite"
        if T == -1%n :#is T = -1 mod n 
            return "A Prime"
    return "A Composite"



n = int(input("Input a number for Miller-Rabin test: "))

print("Given number is : ",Miller_Rabin(n))
