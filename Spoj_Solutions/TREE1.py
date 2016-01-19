factorials={0 : 1 ,
            1 : 1 ,
            2 : 2 ,
            3 : 6 ,
            4 : 24 ,
            5 : 120 ,
            6 : 720 ,
            7 : 5040 ,
            8 : 40320 ,
            9 : 362880 ,
            10 : 3628800 ,
            11 : 39916800 ,
            12 : 479001600 ,
            13 : 6227020800 ,
            14 : 87178291200 ,
            15 : 1307674368000 ,
            16 : 20922789888000 ,
            17 : 355687428096000 ,
            18 : 6402373705728000 ,
            19 : 121645100408832000 ,
            20 : 2432902008176640000 ,
            21 : 51090942171709440000 ,
            22 : 1124000727777607680000 ,
            23 : 25852016738884976640000 ,
            24 : 620448401733239439360000 ,
            25 : 15511210043330985984000000 ,
            26 : 403291461126605635584000000 ,
            27 : 10888869450418352160768000000 ,
            28 : 304888344611713860501504000000 ,
            29 : 8841761993739701954543616000000 ,
            30 : 265252859812191058636308480000000 ,}
def recur(arr):
    if len(arr)<3:
        return 1
    root=arr[0]
    left=[]
    right=[]
    for i in arr[1:]:
        if i<root:
            left.append(i)
        else:
            right.append(i)

    l=len(left)
    r=len(right)
    return fac(l+r)//fac(r)//fac(l)*recur(right)*recur(left)


def fac(n):
    if n in factorials:
        return factorials[n]
    if n==0:
        return 1
    factorials[n]=n*fac(n-1)
    return factorials[n]
    

k=int(input())
for j in range(0,k):
    input()
    n=[int(i) for i in input().split()]
    print(recur(n))
