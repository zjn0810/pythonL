Python类中的self到底是干啥的

Python编写类的时候，每个函数参数第一个参数都是self，一开始我不管它到底是干嘛的，只知道必须要写上。后来对Python渐渐熟悉了一点，再回头看self的概念，似乎有点弄明白了。

首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗（为了和其他编程语言统一，减少理解难度），不要搞另类，大家会不明白的。

下例中将self改为myname一样没有错误：

class Person:
    def _init_(myname,name):
        myname.name=name
    def sayhello(myname):
        print 'My name is:',myname.name
p=Person('Bill')
print p

self指的是类实例对象本身(注意：不是类本身)。

class Person:
    def _init_(self,name):
        self.name=name
    def sayhello(self):
        print 'My name is:',self.name
p=Person('Bill')
print p

在上述例子中，self指向Person的实例p。 为什么不是指向类本身呢，如下例子：

class Person:
    def _init_(self,name):
        self.name=name
    def sayhello(self):
        print 'My name is:',self.name
p1=Person('Bill')
p2 = Person('Apple')
print p1

如果self指向类本身，那么当有多个实例对象时，self指向哪一个呢？

总结

self在定义时需要定义，但是在调用时会自动传入。

self的名字并不是规定死的，但是最好还是按照约定是用self

self总是指调用时的类的实例。
