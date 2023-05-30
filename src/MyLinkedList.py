class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.nextE
        return ' -> '.join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return

        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return

        prev = None
        current = self.head
        while current:
            if current.data == e:
                prev.nextE = current.nextE
                if current == self.tail:
                    self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)

        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return

        if func is None:
            func = lambda a, b: a >= b

        if func(e, self.head.data):
            new_element.nextE = self.head
            self.head = new_element
            self.size += 1
            return

        current = self.head
        while current.nextE and func(current.nextE.data, e):
            current = current.nextE

        new_element.nextE = current.nextE
        current.nextE = new_element
        if current == self.tail:
            self.tail = new_element
        self.size += 1


my_list = MyLinkedList()
my_list.append(5)
my_list.append(2)
my_list.append(7)
my_list.append(1)
my_list.append(9)

print(my_list)

print(my_list.get(7))

my_list.delete(2)

print(my_list)