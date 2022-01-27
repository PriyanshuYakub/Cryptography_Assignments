#include <iostream>
#include <cmath>
#include <algorithm> //to get euclid gcd


using namespace std;


//globally declaring public keys n and e;
int e,n;


bool Divisibility_Test(int n){
	int r = 2;
	while(r<sqrt(n)){
		if(n%r==0){
			return false;
		}
		r++;
	}
	return true;
}

int PrimeGen(){
	int random_number;
	int fn,gn,hn;
	while(true){
		random_number = (rand()%100)+1;
		fn = 2*n + 3;
		gn = pow(n,2) + 1;
		hn = pow(2,n) + 1;

		if(Divisibility_Test(hn)){
			return hn;
		}
		else if(Divisibility_Test(gn)){
			return gn;
		}
		else if(Divisibility_Test(fn)){
			return fn;
		}
		else{
			cout<<"Retrying prime gen";
		}
	}
}

int modInverse(int a, int m){
	for(int i = 1; i<m; i++){
		if(((a%m)*(i%m))%m == 1)
			return i;

	}
	
}

//will return private key d
int Rsa_KeyGen(){
	int p = PrimeGen();
	while(true){
		q = PrimeGen();
		if(p!=q){
			break;
		}
	}

	n = p*q;

	int totient_n = (p-1)*(q-1);

	int cond = 1;
	while(cond == 1){
		e = (rand() % totient_n)+1;
		if(__gcd(e,totient_n)==1){
			cond = 0;
		}
	}
}

int main(){
	cout<<"Hello";
	
}
