#闭包——值
def set_pass(passline):
    def cmp(val):
        if val < passline:
            print('pass')
        else:
            print('failed')
    return cmp


f_100 = set_pass(60)
f_150 = set_pass(90)
#f_100(89)
#f_150(89)

#闭包——函数
def dec(func):
    print('dec start')
    def in_dec(*arg):
        print('in_dec start')
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec

def my_sum(*arg):
    print('my_sum start')
    return sum(arg)

#my_sum = dec(my_sum)
#print(my_sum(1,2,3,4,5,0))


@dec
def my_sum2(*arg):
    print('my_sum start')
    return sum(arg)
print(my_sum2(1,2,3,4,5,0))

#######################################################################
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print ('[%s] %s()...' % (prefix, f.__name__))
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print (test())


import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1)*1000 if unit =='ms' else (t2 - t1)
            print ('call %s() in %f %s'%(f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator
@performance('ms')  
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print (factorial(10))



print('--------------------------------------------')

def log(f):
    print ('log...')
    def wrapper(*args, **kw):
        print ('call...')
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print (f2.__name__)




