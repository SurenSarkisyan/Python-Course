# MRO Method Resolution Order - Порядок вызова метода и иерархия

#    A
#   /  \
#  B    C
#   \  /
#     D


class A:
    def some_method(self):
        print("Method of class A")


class B(A):
    def some_method(self):
        print("Method of class B")


class C(A):
    def some_method(self):
        print("Method of class C")


class D(B, C):
    pass
    def some_method(self):
        print("Method of class D")


# __mro__ - атрибут, mro - метод, или help()

print(D.__mro__)  # узнать иерархию метода
print(D.mro())  # узнать иерархию метода
help(D)  # узнать иерархию метода

some_object = D()
some_object.some_method()



























