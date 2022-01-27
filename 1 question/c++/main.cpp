#include <iostream>
using namespace std;

//simple euclidian algorithm to find gcd of two numbers
int getGcd(int a, int b){
	int r1 = a, r2 = b;
	int q,r;

	while(r2>0){
		q = r1/r2;
		r = r1-q*r2;
		r1 = r2;
		r2 = r; 
	}
	
	return r1;
}

//getting inverse modulo n pf a number using Extended Euclidion Algorithm
int getInverseMod(int n, int b){

	int r1 = n, r2 = b;
	int t1 = 0, t2 = 1;
	int q,r,t;

	while(r2>0){
		q = r1/r2;
		r = r1-q*r2;
		r1 = r2;
		r2 = r; 
		
		//inverse part
		t = t1 - q*t2;
		t1 = t2;
		t2 = t;
	}
	//Getting value in Zn if t1 is -Ve
	if(t1<0){
		t1 = n+t1;
	}
	return t1;
}


//main method
int main(){
	cout<<"Give value of n and b \n";
	int n,b;
	cin>>n;
	cin>>b;

	int gcd = getGcd(n,b);
	cout<<"gcd of " << n << " and " << b << " is: " << gcd << "\n";
	
	//check if inverse exists which is possible only if gcd = 1
	if(gcd == 1){
	int inv_b = getInverseMod(n,b);
	cout<<"inverse of "<<b<<" in modulo "<<n<<" is: "<<inv_b;
	}
	else{
		cout<<"As gcd of given nubers is not equal to 1 inverse modulo of "<<b<<" doesn't exist";
	}


	return 0;
	
}
