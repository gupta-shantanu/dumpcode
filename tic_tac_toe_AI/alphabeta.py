def minmax(arr,depth,alpha,beta):
    if immediatewin(arr,-1*depth):
        return -1*depth
    if full(arr):
        return 0
    value=beta if depth==-1 else alpha
    for i in range(0,9):
        if arr[i]==0:
            arr[i]=depth
            if depth==-1:
                t=minmax(arr,1,alpha,value)
                value=min(value,t)
                arr[i]=0
                if value<alpha:
                    return alpha
            else:
                t=minmax(arr,-1,value,beta)
                value=max(value,t)
                arr[i]=0
                if beta<value:
                    return beta
            
    return value

def full(arr):
    return all(arr[i]!=0 for i in range(0,9))
def immediatewin(arr,depth):
        for i in range(0,3):
            if all(arr[l]==depth for l in [i*3,(i*3+1),(i*3+2)]):
                return True
        for i in range(0,3):
            if all(arr[l]==depth for l in [i,i+3,i+6]):
                return True
        if all(arr[l]==depth for l in [0,4,8]):
            return True
        if all(arr[l]==depth for l in [2,4,6]):
            return True        
        return False

def cmove(arr):
    maxi=-1
    move=0
    for i in range(0,9):
        if arr[i]==0:
            arr[i]=1
            t=minmax(arr,-1,-1,1)
            arr[i]=0
            if maxi<=t:
                maxi=t
                move=i

    return move
def get(arr,j):
    return ('X' if arr[j]==-1 else ('O' if arr[j]==1 else str(j)))
def play():
    arr=[0 for i in range(0,9)]
    for j in range(0,3):
        print(get(arr,j*3),'|',get(arr,j*3+1),'|',get(arr,j*3+2))
        if j!=2:
            print('_________')
    i=0
    while(i<9):
        if i%2==0:
            t=int(input())
            if arr[t]==0:
                arr[t]=-1
            else:
                continue
        else:
            arr[cmove(arr)]=1
        for j in range(0,3):
            print(get(arr,j*3),'|',get(arr,j*3+1),'|',get(arr,j*3+2))
            if j!=2:
                print('_________')
        if immediatewin(arr,-1 if i%2==0 else 1):
            print("and we have a winner")
            break
        i=i+1
    print("End")
    
        
