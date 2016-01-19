#include <stdio.h>
#define max(x,y) ((x>y)? (x):(y))
int main(void) {
	int n,s,lim,i,arr[1005],t,j,a,b,c;
	scanf("%d",&n);
	for(t=1;t<=n;t++){
		scanf("%d %d",&s,&lim);
		for(i=0;i<s;i++)
		scanf("%d ",&arr[i]);

		int dp[s+1][lim+1];
		for(i=0;i<s;i++){
		dp[0][i]=0;
		dp[i][0]=0;
		dp[1][i]=(arr[0]>i) 0:arr[0];
		}
		for(i=2;i<=s;i++){
			for(j=1;j<lim+1;j++){
				a=dp[i-1][j];
				c=arr[i-1];
				if(arr[i-1]>=j)
				{
				b=dp[i-2][j-arr[i-1]]+c;
				dp[i][j]=max(a,b);
				}
				else
				dp[i][j]=max(a,c);
				}
			}
		
		/*
		for(i=0;i<s;i++){
			for(j=0;j<s;j++)
			printf("%d ",dp[i][j]);
			printf("\n");
			}
*/

		printf("Scenario #%d: %d\n",t,dp[s][lim]);
	}
	return 0;
}
