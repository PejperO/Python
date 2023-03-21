name = input("What is your name and surname: ")

one = input("The most common way to spend your free time is for you:"
            "\nwatching TV/movies/series (1)"
            "\nreading books/magazines (2)"
            "\nlistening to music (3)"
            "\nmeetings with family/friends (4)"
            "\ntraveling (5)"
            "\nplaying sports (6)"
            "\nother (7)\n")
if one == "7":
    one = input("Enter: ")

two = input("Under what circumstances do you read books most often:"
            "\nduring the trip (1)"
            "\nduring free time (after work, on vacation) (2)"
            "\nwhile working/studying (it's part of them) (3)"
            "\nI don't read at all (4)"
            "\nother (5)\n")
if two == "5":
    two = input("Enter: ")

three = input("If you spend your free time reading books, what is the main reason for this choice:"
              "\ndesire to expand knowledge (1)"
              "\nreading relaxes me (2)"
              "\nhe fact that reading is fashionable (3)"
              "\nreading is my hobby (4)"
              "\nthe need to study in connection with the work/studies performed (5)"
              "\nI feel family/environmental pressure to read (6)"
              "\nother (7)\n")
if three == "7":
    three = input("Enter: ")

four = input("What kind of books do you read most often:"
             "\npaper (traditional) (1)"
             "\ne-books (electronic books) on your computer (2)"
             "\ne-books on a tablet/phone (3)"
             "\ne-books on a special reader (e.g. Kindle) (4)\n")

five = input("How many books do you read on average per year:"
             "\n0 (1)"
             "\nnone in its entirety - only fragments (2)"
             "\n1 (3)"
             "\n2 or 3 (4)"
             "\n4 - 10 (5)"
             "\nover 10 (6)\n")

six = input("How often do you read books on average:"
            "\nevery day (1)"
            "\nonce a week (2)"
            "\nonce a month (3)"
            "\nonce every few months (4)"
            "\nonce every half year (5)"
            "\nonce a year (6)"
            "\nat all (7)\n")

seven = input("What language do you read books in:"
              "\nEnglish (1)"
              "\nPolish (2)"
              "\nGerman (3)"
              "\nRussian (4)"
              "\nSpanish (5)"
              "\nFrench (6)"
              "\nother (7)\n")
if three == "7":
    three = input("Enter: ")
