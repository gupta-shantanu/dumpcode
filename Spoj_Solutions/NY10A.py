n=int(input())
const=[588, 540, 564, 516, 576, 528, 552]
count={588:0, 540:0, 564:0, 516:0, 576:0, 528:0, 552:0, 504:0}
for j in range(0,n):
	
    b=input()
    a=input()
    p=0
    for i in range(0,len(a)-2):
        key=ord(a[i])+ord(a[i+1])*2+ord(a[i+2])*4
        count[key]+=1
        p+=1
    print(j+1,end=' ')
    for i in const:
        print(count[i],end=' ')
        count[i]=0
        
    print(count[504])
    count[504]=0
    

