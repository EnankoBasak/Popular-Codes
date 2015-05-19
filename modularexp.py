Modulo=10**9 +7 

def power(x,n,m):
	if n == 0:
		return 1
	elif n % 2 == 0 :
		y = power(x,n//2,m)
		return (y * y) % m
	else :
		return ((x % m ) * power(x,n-1,m)) % m
    
    
print ( power(2,Modulo-2,Modulo))
