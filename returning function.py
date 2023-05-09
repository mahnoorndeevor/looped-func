def ret(n):
    def inner(x):
        raised=x**n
        return raised
    return inner

square1=ret(3)
square2=ret(2)
print(square1(4), square2(5))