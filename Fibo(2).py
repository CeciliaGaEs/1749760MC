def fibo(n):
	cnt=0
	if n==0 or n==1:
		return(1)
	r,r1,r2=0,1,2
	for i in range (2,n):
		cnt+=1
		r=r1 + r2
		r2=r1
		r1=r
	return r, cnt
