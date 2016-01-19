#include <stdio.h>
 
int main(void) {
	int n,i,t;
	long c;
	long long clone;
	scanf("%d",&t);
	while(t--){
		clone=1;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%ld",&c);
		clone-=c;
		clone<<=1;
	}
	if(clone==0)
	printf("Yes\n");
	else
	printf("No\n");
	}
	return 0;
}
