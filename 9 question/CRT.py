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

def crt(a_list,m_list):
	#initialising M
	M = 1
	for m in m_list:
		M *= m
	Mi_list= []
	for m in m_list:
		Mi_list.append(M/m)
	invMi_list = []
	for(m,Mi) in zip(m_list,Mi_list):
		invMi_list.append(getModInverse(m,Mi))
	
	x = 0#initialising solution
	list_len = len(m_list)
	for i in range(0,list_len):
		x += a_list[i]*Mi_list[i]*invMi_list[i]
	x = x%M

	return int(x) #not necessary but just to remove decimal 
                  #point which occurs as we used multiplication

def main():   
	m_list = []
	a_list = []
    
	k = int(input("for equations of form - a modulo m \nPlease enter the number of equations: "))
	for i in range (0,k):
		a = int(input("Input a : "))
		m = int(input("Input its coressponding m  : "))
		a_list.append(a)
		m_list.append(m)
	print("using chinese remainder theorem, the value of x for which it is congruent to all given equations is:\n x = ",crt(a_list,m_list))

main()