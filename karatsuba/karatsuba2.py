def karatsuba(x,y):
	if x<10 and y< 10: return x*y
	
	n = max(len(str(x)),len(str(y)))
	m = n / 2
		
	a = int(x / 10**(m))
	b = int(x % 10**(m))
	c = int(y / 10**(m))
	d = int(y % 10**(m))
		
	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	ad_mas_bc = karatsuba(a+b,c+d) - ac - bd
	return int(ac * (10**(2*m)) + ad_mas_bc * (10**m) + bd)
	
print('El resultado es : ', karatsuba(22232432324323454353453454234324324324342343243245452525423542332423432432423432432423,546243243243243243243243243243243243243242345252452352435435432524354235423424234324324234324234227))
print('El resultado es : ', karatsuba(21535220,21535220))