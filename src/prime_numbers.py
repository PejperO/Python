numbers = input("Enter the numbers you want to check if they are prime numbers (separated by commas): ")
numbers_list = numbers.split(",")


def are_primes(*args):
    def is_prime(number):
        number = int(number)
        if number <= 1:
            return False
        elif number <= 3:
            return True
        elif number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    for n in args:
        if is_prime(int(n)):
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime")


are_primes(*numbers_list)
