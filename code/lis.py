
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
    return foldr(lst, lambda head,tail: make_cons(head,tail) if pred(head) else tail,None)

# sort
def sort(lst,pred=lambda a,b: a > b):
    if lst and tail_of(lst):
        return concat(append(head_of(lst), 
                            sort(select(tail_of(lst), lambda e: pred(head_of(lst),e)), 
                                pred)),
                    sort(select(tail_of(lst), lambda e: pred(e,head_of(lst))),
                        pred))
    return lst

