import math
from sympy import symbols, Eq, solve

def Divisibility_test(n):
    r = 2
    while(r<= math.sqrt(n)):
        if(n%r==0):
            return "A composite number"
        r += 1
    return " a prime number "



def main():
    n = int(input("Input number to check if it is prime: "))
    print("Using divisibility test we find that the given number is: ",Divisibility_test(n))

main()