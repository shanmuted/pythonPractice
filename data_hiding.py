class A:
    a=5
    _b=6
    __c=9
    def summ(self):
        print(self.a)
        print(self._b)
        print(self.__c)
class B(A):
    def b(self):
        print("private",self.a)
        print("protected",self._b)q
class C(B):
    def c(self):
        print("public",self.a)
        print("protected",self._b)
o1=C()
o1.summ()
o1.b()
o1.c()