#include <stdio.h>
#define max(x,y) ((x>y)? (x):(y))

void swap(int* a,int* b){
	//printf("%d %d\n",*a,*b);
	//int* c;
	//c=*a;
	//*a=*b;
	//*b=c;
	}
int main(void) {
	int lim,n,i,j,a,b;
	scanf("%d %d",&lim,&n);
	int value[n],weight[n],dop1[lim+1],dop2[lim+1],*dp1,*dp2,*swap;
	dp1=dop1;
	dp2=dop2;
	for(i=0;i<n;i++){
		scanf("%d %d",&value[i],&weight[i]);
	}

	
	for(i=0;i<=n;i++)
	{
		for(j=0;j<=lim;j++)
		{
			if(i==0)
			dp2[j]=0;

			
			else
			{
				a=dp1[j];
				
				if(weight[i-1]<=j)
				{
				b=dp1[j-weight[i-1]]+value[i-1];
				
				dp2[j]=max(a,b);
				}
				else
				dp2[j]=a;
			}
		}
		//swap(&dp1,&dp2);
		swap=dp1;
		dp1=dp2;
		dp2=swap;
	}
	printf("%d\n",dp1[lim]);
	
	return 0;
}
