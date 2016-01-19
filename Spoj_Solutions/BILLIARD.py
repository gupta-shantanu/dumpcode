###include <stdio.h>
###include<math.h>
###define PI 3.1415926535
##int main(void) {
##	int a,b,s,m,n;
##        double angle;
##        while(1)
##		{
##                    scanf("%d %d %d %d %d",&a,&b,&s,&m,&n);
##                    if(a==0 && b==0 && s==0 && m==0 && n==0)
##                    break;
##                    angle=atan((b*n*1.0)/(a*m));
##                    printf("%.2f %.2f",angle*180/PI,(a*m)/s/cos(angle));
##                    
##                    }
##        }

from math import cos,atan,pi,sin
while(1):
    a,b,s,m,n=[int(i) for i in input().split()]
    if a==0 and b==0 and s==0 and m==0 and n==0:
        break
    f=a*m
    if f!=0:
        angle=atan((b*n)/f)
    else:
        angle=1.5707963267948966
    if angle<0.7853981633974483:    
        print("%2.2f %2.2f"%(angle*180/pi,f/s/cos(angle)))
    else:
        print("%2.2f %2.2f"%(angle*180/pi,b*n/s/sin(angle)))
    
        
