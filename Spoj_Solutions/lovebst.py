#include <stdio.h>

int main(void) {
	int n,t,i,dic[1001],k,j;
	dic[0]=1;
	dic[1]=1;
	dic[2]=2;
	dic[3]=5;
	for(i=4;i<1000;i++)
	{
		k=0;
	for(j=0;j<i/2;j++)
	k+=(dic[j]*dic[i-j-1])%1908;
	if(i%2)
	k+=dic[i/2];
	k=(k*2)%1908;
	dic[i]=k;
	}
	
scanf("%i",&t)

	
	while(t--) { 
scanf("%d",&n);
printf("%d",dic[n]);

}
	return 0;
}
