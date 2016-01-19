n=int(input())
for j in range(0,n):
    n,i=[int(l) for l in input().split()]
    print(n**i-(n-2)**i)
