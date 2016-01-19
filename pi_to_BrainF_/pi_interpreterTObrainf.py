##    Author: shantanu
##    TRIVIAL script
##    It converts pi(an esoteic language derived from brainf**) to brainf**

inp=open(input("full name or path of PI file?   "),'r').read()
pi=open("pi.txt",'r').read()

if len(pi)<len(inp):
    print("Script too big for given refernce of pi.txt\n Suggestion: update value of pi.txt to longer precision")
    input()
    assert(0)

arr="> < + - . , [ ]".split()
out=""
for i in range(0,len(inp)-1):
    if inp[i]!=pi[i]:
        if inp[i]>pi[i]:
            out=out+(str(arr[int(inp[i])-1]))
        else:
            out=out+(str(arr[int(inp[i])]))
outfile=open("outinbrainf.txt",'w')
outfile.write(out)
outfile.close()
print("Done... Press Enter To Exit")
input()

    
        
    
