a,b=input().split()
a=int(a)
b=int(b)
lst=[dict() for i in range(0,a+1)]
for i in range(0,b):
    p,q,r,s=input().split()
    p=int(p)
    q=int(q)
    r=int(r)
    s=int(s)
    lst[p][q]=r
    lst[q][p]=s
inputs=[]
outputs=[]
tm=int(input())
hi=0
for i in range(0,tm):
        inp=(int(input()))
        inputs.append(inp)
        outputs.append(0)
        if inp>hi :
                hi=inp

depth=0
curr=1
while(depth<hi):
        c=list(lst[curr].keys())
        tmp=c[0]
        for x in c:
                if(lst[curr][x]<lst[curr][tmp]):
                         tmp=x
        t=lst[curr][tmp]
        lst[curr][tmp]=max(lst[curr].values())+1
        curr=tmp
        depth=depth+1
        if depth in inputs:
                outputs[inputs.index(depth)]=t
                                
                          
                
                       
for depth in range(0,len(outputs)):
        if outputs[depth]!=0:
                print(outputs[depth],"\n")
        else:
                print(outputs[inputs.index(inputs[depth])],"\n")

            



                         
                

                        
                         
                         
                         
                         
                        
                        
                        
               
