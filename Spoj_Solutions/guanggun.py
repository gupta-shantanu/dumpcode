while True:
    try:
        k=input()
    except:
        break
    n=int(k)
    if n<10:
        print(n**2)
    else:
        check=(n-10)//9
        ans=45+44*check
        left=n-check*9-10
        if left:
            ans+=(left+1)**2-1
        ans+=(n-left)//9*37
        print(ans)
        
