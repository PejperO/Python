# Create an iterator class for the list. Use it to insert list1 elements into a string.
# elements are to be in the string one line, not separated by anything:

class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        element = self.lst[self.index]
        self.index += 1
        return str(element)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
iterator = ListIterator(lista1)
wynik1 = "".join(iterator)

print(wynik1)


# Write a function fizzbuzz(n) that uses a combo list to return
# list from 1 to n inclusive numbers or words Fizz, Buzz, FizzBuzz, according to the standard
# game rule in FizzBuzz:
# If the number is divisible by 3 and not divisible by 5, we get "Fizz" instead of the number.
# If the number is divisible by 5 and not divisible by 3, we get "Buzz" instead of the number.
# If the number is both divisible by 3 and by 5, we get "FizzBuzz" instead of the number.
# Write a function fizzbuzz(n) that uses a combo list to return
# list from 1 to n inclusive numbers or words Fizz, Buzz, FizzBuzz, according to the standard
# game rule in FizzBuzz:
# If the number is divisible by 3 and not divisible by 5, we get "Fizz" instead of the number.
# If the number is divisible by 5 and not divisible by 3, we get "Buzz" instead of the number.
# If the number is both divisible by 3 and 5, we get "FizzBuzz" instead of the number.

def fizzbuzz(n):
    return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in
            range(1, n + 1)]


wynik2 = fizzbuzz(16)
print(wynik2)


# Write a generator that returns n terms of the Lucas sequence
# write the 6th element of this string to the result.

def lucas_sequence(n):
    a, b = 2, 1
    yield a
    if n > 1:
        yield b
    count = 2
    while count < n:
        next_element = a + b
        yield next_element
        a, b = b, next_element
        count += 1


generator = lucas_sequence(6)
wynik3 = list(generator)[-1]

print(wynik3)


# Use a class to hold java code characters from Main.java.

class JavaCode:
    def __init__(self):
        self.code = ""

    def read_from_file(self, file_name):
        with open(file_name, "r") as file:
            self.code = file.read()


obiekt = JavaCode()
obiekt.read_from_file("../data/Main.java")
wynik4 = len(obiekt.code)

print(wynik4)


# Write a function that validates the java code using the object from the previous task
# and including only parentheses in the code.
# the function should return True or False depending on whether the code is correct or not.

def validation(kod_o):
    stack = []
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']

    for char in kod_o.code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False

    return len(stack) == 0


obiekt = JavaCode()
obiekt.read_from_file("../data/Main.java")
wynik5 = validation(kod_o=obiekt)

print(wynik5)
