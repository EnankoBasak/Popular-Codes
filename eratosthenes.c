initialise limit and pr[]

void prime()
{
	int i,j;
	for(i=0;i<=limit;i++) pr[i]=true;
	pr[0]=true;
    pr[1]=false;
	for(i=2;i<=limit;i++) if(pr[i])
	for(j=i+i;j<=limit;j+=i) pr[j]=false;
}
