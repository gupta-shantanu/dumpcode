
public class doing
{
		String getexpression(String stg)
{
	doing ob=new doing();
	String stp,tmp;
		stg=stg.replace("asin","asn");
				stg=stg.replace("atan","atn");
					stg=stg.replace("acosec","acc");
						stg=stg.replace("asec","asc");
							stg=stg.replace("acot","act");
								stg=stg.replace("acos","acs");
								stg=stg.replace("cosec","xyz");
	try{
	    for(int i=0;i<stg.length()-3;i++)
	    {
	        stp=stg.substring(i,i+3);
	        if(stp.equals("log"))
	        {
	          


	            stg=stg.substring(0,i)+Math.log(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("sin"))
	        {
	          


	            stg=stg.substring(0,i)+Math.sin(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("cos"))
	        {
	          


	            stg=stg.substring(0,i)+Math.cos(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("tan"))
	        {
	          


	            stg=stg.substring(0,i)+Math.tan(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("sec"))
	        {
	          


	            stg=stg.substring(0,i)+1/Math.cos(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	         if(stp.equals("xyz"))
	        {
	          


	            stg=stg.substring(0,i)+1/Math.sin(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	         if(stp.equals("cot"))
	        {
	          


	            stg=stg.substring(0,i)+1/Math.tan(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	         if(stp.equals("asn"))
	        {
	          


	            stg=stg.substring(0,i)+Math.asin(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("acs"))
	        {
	          


	            stg=stg.substring(0,i)+Math.acos(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("atn"))
	        {
	          


	            stg=stg.substring(0,i)+Math.atan(Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("acc"))
	        {
	          stg=stg.substring(0,i)+Math.asin(1/Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("asc"))
	        {
	           stg=stg.substring(0,i)+Math.acos(1/Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        if(stp.equals("act"))
	        {
	          


	            stg=stg.substring(0,i)+Math.atan(1/Float.parseFloat(ob.getexpression((tmp=ob.clipfunc(stg.substring(i+3))).substring(1,tmp.indexOf('$')-1))))+stg.substring(i+4+Integer.parseInt(tmp.substring(tmp.indexOf('$')+1)));
	       
	        }
	        
	        
	    }
	return (ob.getsolution(ob.getpostfix(ob.addnegative(stg))));
	}
	catch(Exception E)
	{
		
		return "unknown";	
		
	}
	}
String clipfunc(String str)
{
int i,op=0;
for( i=0;i<str.length();i++)
{
if(str.charAt(i)=='(')
op++;
else if(str.charAt(i)==')')
op--;
if(op==0)break;
}
return str.substring(0,i+1)+"$"+i;
}
String getpostfix(String str)
{
String os="";int p=0,top=0;
for(int i=0;i<str.length();i++)
{if(!(Character.isLetterOrDigit(str.charAt(i))))p++;}
char arr[]=new char[p];
p=0;
for(int i=0;i<str.length();i++)
{

if(!(Character.isLetterOrDigit(str.charAt(i)))&&str.charAt(i)!='.')
{
if(str.charAt(i)!='('&&p!=i){
os=os+str.substring(p,i)+"$";}
p=i+1;
if(str.charAt(i)==')')
{
for(int l=top-1;arr[l]!='(';l--){
os=os+arr[l];
top--;}
top--;
continue;
}
while(true)
{
if(top==0){
arr[top++]=str.charAt(i); break;
}
else
{
if(arr[top-1]=='('){
arr[top++]=str.charAt(i);break;}
else if(priority(str.charAt(i),arr,top))
{
arr[top++]=str.charAt(i);
break;
}
else
{
os=os+arr[--top];
}
}}
}
}
if(str.length()>p)
{
if(str.charAt(p)!=')')
os=os+str.substring(p)+"$";
}
for(int i=top-1;i>-1;i--)
os=os+arr[i];
return os;
}
boolean priority(char ch,char arr[],int top)
{
int flag=0;
String pri[]={"^","*/%","-+"};
for(int i=0;i<3;i++)
{
if(pri[i].indexOf(ch)!=-1)
{
for(int j=0;j<=i;j++)
{
if(pri[j].indexOf(arr[top-1])!=-1){
flag++;break;}
}
break;
}
}
return (flag==0)? true:false;
}
String getsolution(String st)
{
int top=0;
for(int i=0;i<st.length();i++)
top=(st.charAt(i)=='$')? top+1:top;
int p=0;
double a,b,arr[]=new double[top];
top=0;
for(int i=0;i<st.length();i++)
{
if(st.charAt(i)=='$')
{
arr[top++]=Double.parseDouble(st.substring(p,i));
p=i+1;
}
else if(!(Character.isLetterOrDigit(st.charAt(i)))&&st.charAt(i)!='.')
{
p=i+1;
a=arr[--top];
b=arr[--top];
if(st.charAt(i)=='^')
arr[top++]=Math.pow(b,a);
if(st.charAt(i)=='+')
arr[top++]=b+a;
if(st.charAt(i)=='-')
arr[top++]=b-a;
if(st.charAt(i)=='*')
arr[top++]=b*a;
if(st.charAt(i)=='/')
arr[top++]=b/a;
if(st.charAt(i)=='%')
arr[top++]=b%a;
}
}
return String.valueOf(arr[0]);
}
String addnegative(String str)
{
if(str.charAt(0)=='-')
str="(0-1)*"+str.substring(1);
for(int i=(str.indexOf('-')<0)?str.length(): str.indexOf('-') ;i<str.length();i++)
{
if(str.charAt(i)=='-')
{
if(!Character.isLetterOrDigit(str.charAt(i-1))&&str.charAt(i-1)!='.'&&str.charAt(i-1)!=')')
str=str.substring(0,i)+"(0-1)*"+str.substring(i+1);
}
}
return str;
}
}
