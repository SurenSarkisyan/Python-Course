object={"car","door","car"}
print(object)


class myClass:
    i = 0
    def __init__(self):
        i = 1
obj = myClass()
print(obj.i)


a = [1, 2, 3]
if a[2] <3:
    print(a[a[1]])
else:
    print(a[1])



def factorial(n):
    if n == 0:
        return  1
    else:
        return n * factorial(n -1)
print(factorial(5))


Greeting = "Hello World"
a = Greeting[0]
print(a)
b = Greeting[6]
print(b)
c = Greeting[11]
print(c)






