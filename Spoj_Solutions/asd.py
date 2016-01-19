class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A=list(set(A))
        A.sort()
        seq=1
        mx=0
        prev=-21398889
        sr=[]
        for i in A:
            #print(i,A,seq,mx)
            if i==prev+1:
                seq+=1
                sr.append(i)
            else:
                if seq>mx:
                    mx=seq
                    seq=1
                    mr=sr.copy()
                    sr=[]
            prev=i
        if seq>mx:
            mx=seq
            mr=sr.copy()
                    
        return mx,mr     
                
                
                
