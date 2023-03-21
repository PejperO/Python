a = b = c = "Python 2023"


def out():
    print(a == b)
    print(b == c)
    print(type(a), type(a), type(a))
    print(hex(id(a)))
    print(hex(id(b)))
    print(hex(id(c)))


out()
c = "Java 11"
out()
