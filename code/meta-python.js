
function fib(n){
	var v = c = 1;
	var res = 1;
	while(1){
		if(n == 0 || n == 1)
			return res;
		n--;
		res = v+c;
		v = c;
		c = res;
	}
}

/**
def Pair(x,y):
	return lambda(f): f(x,y);
def first(x,y):
	return x
def rest(x,y):
	return y
*/
function Pair(x,y){
	return function (fun){
		return fun(x,y);
	}
}

function first(a,b){
	return a;
}

function rest(a,b){
	return b;
}

var p = Pair(1,2);
p(first); //; => 1


function MutablePair(a,b){
	return function(f){
		var x = f(a,b);
		a = x(rest)(first);
		b = x(rest)(rest)(first);
		return x(first);
	};
}

function get_first(a,b){
	return Pair(a, Pair(a, Pair(b, null)));
}

function get_rest(a,b){
	return Pair(b, Pair(a, Pair(b, null)));
}

function set_first(value){
	return function (a,b){
		return Pair(value, Pair(value, Pair(b, null)));
	};
}

function set_rest(value){
	return function (a,b){
		return Pair(value, Pair(a, Pair(value, null)));
	};
}

var mp = MutablePair(1,2);
mp(get_first); //; => 1
mp(set_first(2));
mp(get_first); //; => 2

/**
Pair( <retval>,
	Pair( <val_a>,
		Pair( <val_b>, null)
	)
);
*/


function MutablePair2(x,y){
	var _this = {
		get_first: function(){return x;},
		get_rest: function(){return y;},
		set_first: function(value){x = value;return value;},
		set_rest: function(value){y = value;return value;},
	};
	return _this;
}

var mp2 = new MutablePair2(1,2);
mp2.get_first() //; => 1
mp2.set_first(3)
mp2.get_first() //; => 2

function xfib_range(a,e){
	return function(){
		if (a != e){
			return fib(a++);
		}else{
			throw undefined;
		}
	};
}

rng = xfib_range(0,11);
rng() //; => 1
rng() //; => 1
rng() //; => 2

function yfib_range(a,e){
	c = a
	return function(fun){
		var x = fun(a,e,c);
		c = x[1];
		return x[0];
	}
}

function fib_forward(a,e,c){
	if(c < e){
		return [fib(c),c+1];
	}else{
		throw undefined;
	}
}

function fib_backward(a,e,c){
	if(c > a){
		return [ fib(c-1),c-1];
	}else{
		throw undefined;
	}
}

function fib_seek(i){
	return function(a,e,c){
		if(a + i < e){
			return [ fib(a+i),c ];
		}else{
			throw undefined;
		}
	};
}

rng2 = yfib_range(1,500000);
rng2(fib_forward); //; => 1
rng2(fib_forward); //; => 2
rng2(fib_forward); //; => 3
rng2(fib_forward); //; => 5
rng2(fib_backward); //; => 5
rng2(fib_backward); //; => 3
rng2(fib_seek(0)); //; => 1
rng2(fib_seek(3)); //; => 5

