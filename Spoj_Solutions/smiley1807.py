#include <stdio.h>
#define max(x,y) ((x>y)? (x):(y))
#define LEN 1000000
int main(void) {
	int i,j,a,b,last;
        char st[LEN],ch;
	scanf("%s",&st);
	int dp1[LEN];
    char smiley[]={'1','8','0','7'};
	for(j=1;st[j]!='\0';j++)
		{
                    dp1[j]=0;
                    }

	last=0;
	/*
	for(i=0;i<4;i++)
	{
		for(j=1;(ch=st[j-1])!='\0';j++)
		{
                    
                    
			if(ch==smiley[i] && (dp1[j]!=0 || i==0))
                        {
                        a=dp1[j]+1;
                        b=dp2[j-1]+1;
			dp2[j]=max(a,b);
                        }			
			else
			dp2[j]=dp2[j-1];
		}
		//swap(&dp1,&dp2);
		swap=dp1;
		dp1=dp2;
		dp2=swap;
	}
	printf("%d\n",dp1[j-1]);
	*/
	return 0;
}
