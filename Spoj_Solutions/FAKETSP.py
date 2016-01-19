a=input()[-80:].split()

x=float(a[-2][1:-1])
y=float(a[-1][:-2])
s=0
while True:
    try:
        a=input()[-80:].split()
    except:
        break
    x2=float(a[-2][1:-1])
    y2=float(a[-1][:-2])
    s+=((x2-x)**2+(y2-y)**2)**0.5
    print("The salesman has traveled a total of %.3f kilometers."%s)
    x=x2
    y=y2
    

