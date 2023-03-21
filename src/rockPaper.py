import getpass
import random


def who_won():
    if choice1 == "1":
        if choice2 == "1":
            return 0
        if choice2 == "2":
            return 2
        if choice2 == "3":
            return 1
    if choice1 == "2":
        if choice2 == "1":
            return 2
        if choice2 == "2":
            return 0
        if choice2 == "3":
            return 2
    if choice1 == "3":
        if choice2 == "1":
            return 2
        if choice2 == "2":
            return 2
        if choice2 == "3":
            return 0


rounds = input("how many rounds: ")
rounds = int(rounds)
game_mode = input("computer (1) || 2 players (2): ")

Player1 = input("player's 1 name: ")
points1 = points2 = 0

if game_mode == "2":
    Player2 = input("player's 2 name: ")

    for i in range(1, rounds + 1):
        print("Round " + str(i))
        print(Player1 + " turn")
        choice1 = getpass.getpass("Rock(1), Paper(2), scissors(3)")
        print(Player2 + " turn")
        choice2 = getpass.getpass("Rock(1), Paper(2), scissors(3)")

        win = who_won()
        if win == 0:
            print("draw")
            points1 += 1
            points2 += 1
        if win == 1:
            print("point for " + Player1)
            points1 += 1
        if win == 2:
            print("point for " + Player2)
            points2 += 1

else:
    Player2 = "Computer"

    for i in range(1, rounds + 1):
        print("Round " + str(i))
        choice1 = input("Rock(1), Paper(2), scissors(3)")
        choice2 = str(random.randint(1, 3))

        win = who_won()
        if win == 0:
            print("draw")
            points1 += 1
            points2 += 1
        if win == 1:
            print("point for " + Player1)
            points1 += 1
        if win == 2:
            print("point for " + Player2)
            points2 += 1

if points1 > points2:
    print(Player1 + " WON")
if points2 > points1:
    print(Player2 + " WON")
if points2 == points1:
    print("draw")

print("SCORE - " + str(points1) + " : " + str(points2))
