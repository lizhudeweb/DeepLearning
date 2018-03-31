#############函数调用#################
def f():
    print ('call f()...')

    def g():
        print ('call g()...')
        return 0
    return g
a = f()
#b = a()
print (a())

#############闭包#################
print ('-------------')
def count():
    fs = []
    for i in range(1, 4):
        print(i)
        def f():
            print(i)
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
#f1=count()[0],f2=count()[1],f3=count()[2].

print (f1())
print (f2())
#print (f3())
#print (f1, f2, f3)
print ('-------------')
def count():
    fs = []
    for i in range(1, 4):
        def f(m = i):
            return m * m
        fs.append(f)
    return fs

#f1, f2, f3 = count()

#print (f1(), f2(), f3())
c = count()[0]
print(c());




