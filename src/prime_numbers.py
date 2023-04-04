number = int(input("Enter the number you want to check if it is a prime number: "))


def is_prime():
    if number <= 1:
        return "not prime"
    elif number <= 3:
        return "prime"
    elif number % 2 == 0 or number % 3 == 0:
        return "not prime"
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return "not prime"
        i += 6
    return "prime"


print("Number " + str(number) + " is " + is_prime())
