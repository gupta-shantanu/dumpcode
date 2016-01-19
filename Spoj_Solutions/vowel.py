def vow(st=""):
    ans=" "
    st="a"+st
    vowel="a e i o u A E I O U".split()
    for i in range(1,len(st)):
        n= "V" if (((st[i]=='y' or st[i]=='Y') and not(st[i-1] in vowel)) or (st[i] in vowel)) else "C"
        if ans[len(ans)-1]!=n:
            ans=ans+n
        
    return ans[1:]
print(vow("yoghurt"))
print(vow("YipPy"))
print(vow("SYZYGY"))
    
