def simulateParlor(i,st):
    ans=0;
    inside=[]
    service=[]
    for k in st:
        if not(k in inside):
            inside.append(k)
            if len(service)<i :
                service.append(k)
        elif (k in inside) and (k in service):
            inside.remove(k)
            service.remove(k)
        elif k in inside and not(k in service):
            inside.remove(k)
            ans=ans+1
    return ans

print(simulateParlor (2, "ABBAJJKZKZ"))

print(simulateParlor (3, "GACCBDDBAGEE"))

print(simulateParlor (3, "GACCBGDDBAEE"))

print(simulateParlor (1, "ABCBCA"))


        
                
            
