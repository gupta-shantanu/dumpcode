#include <stdio.h>
#define max(x,y) ((x>y)? (x):(y))

int main(void) {
	int lim,n,i,j,a,b;
	scanf("%d %d",&lim,&n);
	int value[n],weight[n],dp[lim];
	for(i=0;i<n;i++){
		scanf("%d %d",&value[i],&weight[i]);
	}
	for(j=lim-weight[0];j<lim;j++)
	dp[j]=0;
	dp[0]=0;
	for(i=0;i<n;i++)
	{
		if(lim-weight[i]-1<0)continue;
		for(j=lim-weight[i]-1;j>=0;j--)
		{
			a=dp[j+weight[i]-1];
			b=dp[j-1]+value[i];
				dp[j+weight[i]-1]=max(a,b);
			
		}
	}
	printf("%d\n",dp[lim]);
	
	return 0;
}
