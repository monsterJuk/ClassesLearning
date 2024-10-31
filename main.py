class C2():
    def f2(self):
        pass


class C3():
    def f3(self):
        pass


class C1(C2, C3):
    def setname(self, name):
        self.name = name


I1 = C1()
I2 = C1()

I1.setname('Bob')

print(I1.name)
