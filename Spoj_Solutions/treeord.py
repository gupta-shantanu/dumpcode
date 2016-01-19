#include <stdio.h>
int dic[8001],pre[8001],post[8001],ino[8001];

bool check(pr1,pr2,ps1,ps2,in1,in2)
{
    if(pre[pr1]!=post[pr2])
    return false;
    
    root=dic[pre[pr1]];
    return check(pr1+1,pr1+root,ps1,ps1+root,0,root-1)&&check(pr2);
    
    }


int main(void) {

int t;
scanf("%i",&t)
int n,i,pre[t],post[t],ino[t],j;
for(i=0;i<t;i++)
{
 scanf("%i",&pre[i]);   
    }
for(i=0;i<t;i++)
{
 scanf("%i",&post[i]);   
    }
for(i=0;i<t;i++)
{
 scanf("%i",&ino[i]);   
    }
    for(i=0;i<8000;i++)
    {
dic[ino[0]]=i;
        }
if(check(0,t,0,t,0,t))
printf("yes");
else
printf("no");

	return 0;
}
