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

reversed(sorted(lst))
#; => [89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

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

def fib_range(s,e):
    lst = []
    for i in range(s,e):
        lst.append(fib(i))
    return lst

'''
>>> lst_2 = fib_range(0,100000)
'''

class xfib_range:
    def __init__(self,s,e):
        self.start = s
        self.end   = e
    def __iter__(self):
        return self
    def next(self):
        if self.start != self.end:
            res = fib(self.start)
            self.start += 1
            return res
        else:
            raise StopIteration()

def x2fib_range(s,e):
    for i in xrange(s,e):
        yield fib(i)

#; ===========================================
#
## reference
#
#  http://srfi.schemers.org/srfi-1/srfi-1.html
#
## structure
#
#  LIST(1,2,3)  => 
#    CONS(1,
#       CONS(2,
#           CONS(3, None)))
##

## constructors
def make_cons(first,rest):
    return lambda fun: fun(first,rest)

def make_list(lead,*rest):
    if rest :
        return make_cons(lead,make_list(*rest))
    else:
        return make_cons(lead,None)

## helper function
def head_of(lst):
    return lst(lambda head,tail:head)

def tail_of(lst):
    return lst(lambda head,tail:tail)

def print_list(lst):
    if lst :
        print head_of(lst),
        print_list(tail_of(lst))
    else:
        pass


lst = make_list(1,2,3,4,5)
print_list(lst) #; >> 1 2 3 4 5

print head_of(lst) #; >> 1
print_list(tail_of(lst)) #; >> 2 3 4 5

## utilities

def length(lst,len=0):
    if lst:
        return length(tail_of(lst),len+1)
    return len

def append(elem,lst):
    if lst:
        return make_cons(head_of(lst),append(elem,tail_of(lst)))
    return make_cons(elem,None)

def concat(lst1,lst2):
    if lst1:
        return make_cons(head_of(lst1),concat(tail_of(lst1),lst2))
    return lst2

def take(lst,n = 0):
    if n:
        return make_cons(head_of(lst),take(tail_of(lst),n-1))
    return None

def drop(lst,n = 0):
    if n:
        return drop(tail_of(lst), n-1)
    return lst

# each
def each(lst,fn):
    if lst:
        fn(head_of(lst))
        return each(tail_of(lst),fn)
    return None

# map
def collect(lst,fun):
    if lst:
        return make_cons(fun(head_of(lst)),collect(tail_of(lst),fun))
    return None

# filter
def select(lst,pred):
    if lst:
        if pred(head_of(lst)):
            return make_cons(head_of(lst),select(tail_of(lst),pred))
        return select(tail_of(lst),pred)
    return None

# reduce
def foldl(lst,fun,default):
    if lst:
        return fun(foldl(tail_of(lst),fun,default), head_of(lst))
    return default

def foldr(lst,fun,default):
    if lst:
        return fun(head_of(lst), foldr(tail_of(lst),fun,default))
    return default

def collect_over_fold(lst,fun):
    return foldr(lst,lambda head,tail: make_cons(fun(head),tail),None)

def select_over_fold(lst,pred):
    return foldr(lst, 
            lambda head,tail: make_cons(head,tail) if pred(head) else tail,
            None)

# sort
def sort(lst,pred=lambda a,b: a > b):
    if lst and tail_of(lst):
        return concat(append(head_of(lst), 
                            sort(select(tail_of(lst), lambda e: pred(head_of(lst),e)), 
                                pred)),
                    sort(select(tail_of(lst), lambda e: pred(e,head_of(lst))),
                        pred))
    return lst

def out(e):
    print e

##; ** typed **

# primitives to predicates
(pint,pstr,plong,pfloat,pcomplex,pbool) = map(lambda t: 
                                lambda v: type(value(v)) == t, 
                           [int,str,long,float,complex,bool])

# primitive assertion
primitive = lambda obj: type(typeof(obj)) == type

def new(t,v):
    if(t(v)):
        return lambda fn: fn(t,v)
    raise TypeError("invalid type predicate")

def typeof(obj):
    try:
        return obj(lambda t,v: t) ## self defined type
    except:
        return type(obj)  ## primitives

def value(obj):
    try:
        return obj(lambda t,v: v)
    except:
        return obj

## value equality
def eqv(a,b):
    return value(a) == value(b)

## total equality
def eql(a,b):
    return typeof(a) == typeof(b) and value(a) == value(b)

## example types
# natural => (int | long) & (: >= 0)
nat = lambda v: (pint(v) or plong(v)) and v >= 0
# real => int | long | float
real = lambda v: (pint(v) or plong(v) or pfloat(v))
# number => real | complex
num = lambda v: (real(v) or pcomplex(v))
# list<T> => [ T,... ] | None
t_list = lambda t: lambda v: v == None or foldl(v,
            lambda p,e: p and t(e),True)

## example functions
def t_head_of(t):
    return lambda lst: head_of(value(lst)) if t_list(t)(value(lst)) else None
## example constructors
N  = [new(nat,x) for x in range(1<<16)]  # N[x]  => (nat,x)
CI = [new(pint,x) for x in range(1<<16)] # CI[x] => (pint,x)
CL = [new(pint,x) for x in range(1<<16)] # CL[x] => (plong,x)
