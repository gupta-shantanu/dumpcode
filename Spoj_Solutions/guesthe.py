def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

while(True):
    a=input()
    if a=='*':
        break
    num=1
    right=True
    for i,j in enumerate(a):
        if i==0:
            if j=='N':
                print(0)
                right=False
            continue
        if num%(i+1):
            if j=='Y':
                num*=(i+1)//gcd(num,i+1)
                print(i+1,j,num)
        elif j=='N':
                right=False
                print(-1)
                break
    if right:
        print(num)
    
                
        
