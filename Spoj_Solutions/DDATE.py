import sys,calendar as c
input()
for n in input():
 n=int(n)
 print(n&31,c.month_name[(n&480)>>5],n>>9)
