import java.awt.*;

import java.applet.*;
public class app extends Applet
{
int prevx,prevy,pos;
String str,tmp,stg;
public void init()
{
stg=str="";
pos=0;
}
doing ob=new doing();
public void paint( Graphics g ) {
pos=0;
setBackground(Color.white);
for(int i=0;i<21;i++)
{
g.setColor(Color.yellow);
g.drawLine(0,getHeight()/20*i+5,getWidth(),getHeight()/20*i+5);
g.drawLine(getWidth()/20*i,0,getWidth()/20*i,getHeight());
 if(i-10>0) g.setColor(Color.blue); else g.setColor(Color.red);
  if(i==10) g.setColor(Color.green);
g.drawString(-1*(i-10)+"",getWidth()/2+2,getHeight()/20*i+5);
 if(i-10<0) g.setColor(Color.blue); else g.setColor(Color.red);
         
if(i==10)continue;
g.drawString((i-10)+"",getWidth()/20*i,getHeight()/2-2);
}
g.setColor(Color.black);
g.drawLine(getWidth()/2,0,getWidth()/2,getHeight());
g.drawLine(0,getHeight()/2,getWidth(),getHeight()/2);
if(str.equals("help,$"))
{
g.setColor(Color.white);
g.fillRect(getWidth()/2-250,getHeight()/2-20,500,85);
g.setColor(Color.red);
g.drawString("examples: y=(x-1)*(x-2)*(x-3) , y=(sin(x^2-2)^2 or :sin(x) , acos(x) (i.e. inverse), (tan(x))^2 etc.",10,getHeight()/2);
g.drawString("Supports max. 5 graphs at a time(separated by comma,no spaces anywhere)",10,getHeight()/2+20);
g.drawString("To use Calculater type a expression free from 'x' e.g: sin(2)+log(8-4*(2/2))",10,getHeight()/2+35);
}
else if(str!="")
{
if(str.indexOf('=')>0)
str=str.substring(str.indexOf('=')+1);
if(str.indexOf('x')!=(-1))
{
for(int j=0;j<5;j++){
        		  stg=str.substring(pos,(pos=str.indexOf(",",pos)));
        		  if(stg.indexOf('=')>0)
        	          stg=stg.substring(stg.indexOf('=')+1);
        		  if(j==0)
          g.setColor(Color.red);
        		  else if(j==1)
        	          g.setColor(Color.green);
        		  else if(j==2)
        	          g.setColor(Color.blue);
        		  else if(j==3)
        	          g.setColor(Color.black);
        		  else if(j==4)
        	          g.setColor(Color.cyan);
        		  g.drawString(stg,getWidth()*3/4+5,getHeight()/8+j*10);
          prevx=-10;
          prevy=(int)Float.parseFloat(ob.getexpression(stg.replace("x","("+(-10)+")")));
    for(int i=-1*250;i<250;i++){
if(!(tmp=ob.getexpression(stg.replace("x","("+(i/25.0)+")"))).equals("unknown"))//&&tmp!="NaN"
g.drawLine(prevx,prevy,prevx=i+getWidth()/2,prevy=getHeight()/2-(int)(Float.parseFloat(tmp)*25));
}
 if(str.indexOf(",",++pos)<0)break;
          
          }
        	  pos=0;  
}
else{
 if(str.indexOf('=')>0)
                  str=str.substring(str.indexOf('=')+1);
        	  str=str.substring(0,str.indexOf(','));
g.setColor(Color.white);
g.fillRect(getWidth()/2-250,getHeight()/2-20,500,40);
g.setColor(Color.red);
g.drawString("Answer: "+ob.getexpression(str),getWidth()/2,getHeight()/2);
}
g.setColor(Color.blue);
g.drawString("Author:Shantanu Gupta",getWidth()-200,getHeight()-50);
}

}
}