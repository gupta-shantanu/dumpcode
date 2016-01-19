import alphabeta as a
import minmax as m
import time as tk
def play():
    arr=[0 for i in range(0,9)]
    for j in range(0,3):
        print(a.get(arr,j*3),'|',a.get(arr,j*3+1),'|',a.get(arr,j*3+2))
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
            t=tk.clock()
            c=m.cmove(arr)
            print(tk.clock()-t," seconds for minmax",c,"as the answer")
            t=tk.clock()
            d=a.cmove(arr)
            print(tk.clock()-t," seconds for alpha-beta pruned minmax",d,"as the answer")
            arr[d]=1
        for j in range(0,3):
            print(a.get(arr,j*3),'|',a.get(arr,j*3+1),'|',a.get(arr,j*3+2))
            if j!=2:
                print('_________')
        if a.immediatewin(arr,-1 if i%2==0 else 1):
            print("and we have a winner")
            break
        i=i+1
    print("End")
play()
