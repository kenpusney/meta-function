def fib(n):
	if n==0 or n==1:
		return 1
	else:
		a = 1
		b = 1
		c = 0
		for i in range(2,n+1):  #just like for(i = 2; i<=n ; ++i)
			c = a+b
			a = b
			b = c
		return c


def fib_2(n):
	if n==0 or n==1:
		return 1
	else:
		a,b = 1,1
		for i in range(2,n+1):
			a,b = b,a+b
		return b

def fib_3(n):
	if n==0 or n==1:
		return 1
	else:
		return fib_3(n-1) + fib_3(n-2)

def fib_helper(n,v,c):
	if n == 0 or n == 1:
		return c
	else:
		return fib_helper(n-1,c,v+c)

def fib_4(n):
	return fib_helper(n, 1, 1)

def fib_5(n,v=1,c=1):
	if n == 0 or n == 1:
		return c
	else:
		return fib_5(n-1,c,v+c)

def fib_6(n,v=1,c=1):
	if n == 0 or n == 1:
		return c
	else:
		n,v,c = n-1,c,v+c
		return fib_6(n,v,c)

def fib_7(n):
	v,c = 1,1
	while 1:
		if n == 0 or n == 1:
			return c
		n = n-1
		v,c = c,v+c

lst = [1,1,2,3,5,8,13,21,34,55,89]
sorted(lst) #; => [1,1,2,3,5,8,13,21,34,55,89]

lst_1 = sorted(lst)
lst_1.reverse()

def lst_comparator(o1,o2):
	return o2-o1
sorted(lst,lst_comparator)
#; => [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

lst_comparator2 = lambda o1,o2: o2-o1
sorted(lst,lst_comparator2)
#; => [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

sorted(lst,lambda o1,o2:o2-o1)
#; => [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

sorted(lst,lambda o1,o2:-1)
#; => [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

sum(map(lambda a:a**2,lst))
#; => 12816
reduce(lambda e,v: e+v**2,lst)
#; => 12816

def spliter(n):
	return lambda a,b: a-n
sorted(lst,spliter(9))
#; => [8, 5, 3, 2, 1, 1, 13, 21, 34, 55, 89]

class Pair:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def first(self):
		return self.x
	def rest(self):
		return self.y

p = Pair(1,2)
a = p.first()

