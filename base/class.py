class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    #def whoAmI(self):
        #return 'I am a Teacher, my name is %s' % self.name

def who_am_i(x):
    print (x.whoAmI())

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

#print(p.whoAmI())
#print(s.whoAmI())
#print(t.whoAmI())
who_am_i(p)
who_am_i(s)
who_am_i(t)
#.whoAmI()总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止

class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.score < s.score:

            return 1

        elif self.score > s.score:

            return -1

        else:

            if self.name < s.name:

                return -1

            elif self.name > s.name:

                return 1

            else:

                return 0
            
        #if self.name < s.name:
        #    return -1
        #elif self.name > s.name:
        #    return 1
        #else:
            return 0
a = Student1('Tim', 99)
b = Student1('Bob', 88)
c = Student1('Alice', 77)
L = [a,b,c]
        #L = [Student1('Tim', 99), Student1('Bob', 88), Student1('Alice', 77)]
#print(sorted(L))




def a(L):
    for s in L:
        if isinstance(s,Student):
            pass
        else:
            return 'Bug'
b = a(L)
if b == 'Bug':
    print (b)
else:
    print (sorted(L))

 
