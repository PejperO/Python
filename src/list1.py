import random

# 1. How many unique items are in the list:
list_1 = [0, 7, 8, 3, 3, 0, 7, 0, 3]

unique_elements = set(list_1)
w_1 = len(unique_elements)
print(w_1)

# 2. Write code that replaces a random character from a string
s_2 = "ala ma kota"
# to '0':

s_2_list = list(s_2)
index = random.randint(0, len(s_2_list) - 1)
s_2_list[index] = '0'
w_2 = ''.join(s_2_list)
print(w_2)

# 3. Write the code that will replace the R programming language with JS from list_3, then display the replaced JS.
# Before JS, there must still be a python structure of the same type as in the example list_3.

list_3 = [[{1: 'java', 0: ('python', 'R')}, 'c++'], ['word', 'excel']]

for i in list_3:
    if type(i) == list:
        for j in i:
            if isinstance(j, dict):
                for k, v in j.items():
                    if v == 'R':
                        j[k] = 'JS'

w_3 = str(list_3)
print(w_3)

# 4. What type of data from the following cannot be dictionary keys?
# boolean,float,int,string,tuple,list,set. Put the answer in the string w_4

w_4 = "list,set"
print(w_4)

# 5. For a string, print the number of times the given character appeared, in alphabetical order.
# Use a dictionary - the result is also supposed to be a dictionary.
# We check only those characters that appear in the given string.

s_5 = "ala ma kota imie ma macko"

how_many = {}
for char in s_5:
    if char.isalpha():
        if char in how_many:
            how_many[char] += 1
        else:
            how_many[char] = 1

w_5 = dict(sorted(how_many.items()))
print(w_5)

# 6. Write code that will check if in the previous string s_5,
# # any character occurred exactly 3 times. Display Yes if present,
# # Not if it didn't occur.

for char in s_5:
    if s_5.count(char) == 3:
        w_6 = "Tak"
        break
else:
    w_6 = "Nie"

print(w_6)


# 7. Write a function that checks if given words/sentences are palindromes
# # and will return True or False ( is/is not).
# # Skip non-letter characters, case-insensitive

def palindromes(palin):
    palin = ''.join(filter(str.isalpha, palin)).lower()
    return palin == palin[::-1]


s_7_1 = "Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindromes(s_7_1))


# 8. Write a function that will return
# # all numbers from 1 to n in one string separated by commas,
# # however, if the number is divisible by:
# # three - instead of a number we have "Fizz",
# # five - instead of a number we have "Buzz",
# # three and five instead of a number we have "FizzBuzz".
# # all numbers/words are to be returned on one line, separated by a comma
# # Without space

def fizzbuzz(n):
    output = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output += "FizzBuzz"
        elif i % 3 == 0:
            output += "Fizz"
        elif i % 5 == 0:
            output += "Buzz"
        else:
            output += str(i)
        if i < n:
            output += ","
    return output


n_8 = 16
print(fizzbuzz(n_8))

# 9. Write a function that returns the nth element of the Fibonacci sequence
# # with F(0)= 0 and F(1) = 1.
# # without recursion:

n_9 = 6


def fibonacci(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b


print(fibonacci(n_9))


# 10. Write a function that for a given sorted list
# # will return the index of the searched item using binary search,
# # or will return None when there is no element in the list:

def binary_search(lista, e):
    left, right = 0, len(lista) - 1
    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == e:
            return mid
        elif lista[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
    return None


l_10 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
print(binary_search(l_10, 2))
