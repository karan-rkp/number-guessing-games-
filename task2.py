import random
import os
from colorama import init, Fore, Style

init(autoreset=True)


# ===========================
# Utility Functions
# ===========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    clear()
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "          🎯 GUESS THE NUMBER GAME 🎯")
    print(Fore.CYAN + "=" * 60)


def pause():
    input(Fore.WHITE + "\nPress Enter to continue...")


# ===========================
# Difficulty Selection
# ===========================

def choose_level():

    while True:

        header()

        print(Fore.GREEN + "Select Difficulty Level\n")

        print(Fore.YELLOW + "1. Easy")
        print("   Range : 1 - 50")
        print("   Attempts : 10\n")

        print(Fore.CYAN + "2. Medium")
        print("   Range : 1 - 100")
        print("   Attempts : 8\n")

        print(Fore.RED + "3. Hard")
        print("   Range : 1 - 500")
        print("   Attempts : 12\n")

        choice = input(Fore.WHITE + "Enter Choice (1-3): ")

        if choice == "1":
            return 50, 10

        elif choice == "2":
            return 100, 8

        elif choice == "3":
            return 500, 12

        else:
            print(Fore.RED + "\nInvalid Choice!")
            pause()


# ===========================
# Rating
# ===========================

def performance(total_attempts, used):

    score = total_attempts - used

    print("\n" + Fore.CYAN + "=" * 60)

    if used <= total_attempts // 3:
        print(Fore.GREEN + "🏆 Rating : Excellent!")

    elif used <= total_attempts // 2:
        print(Fore.CYAN + "⭐⭐ Rating : Great!")

    elif used <= total_attempts - 2:
        print(Fore.YELLOW + "👍 Rating : Good!")

    else:
        print(Fore.MAGENTA + "😊 Rating : Keep Practicing!")

    print(Fore.CYAN + "=" * 60)


# ===========================
# Main Game
# ===========================

def play():

    maximum, max_attempts = choose_level()

    secret = random.randint(1, maximum)

    attempts = 0

    while attempts < max_attempts:

        header()

        print(Fore.CYAN + f"Guess a Number Between 1 and {maximum}")
        print(Fore.MAGENTA + f"Attempts Left : {max_attempts-attempts}")
        print("-" * 60)

        try:

            guess = int(input(Fore.WHITE + "Enter Your Guess : "))

            if guess < 1 or guess > maximum:
                print(Fore.RED + f"\nEnter a number between 1 and {maximum}.")
                pause()
                continue

            attempts += 1

            if guess < secret:

                print(Fore.YELLOW + "\n📉 Too Low!")

                difference = secret - guess

                if difference <= 5:
                    print(Fore.GREEN + "🔥 Very Close!")

            elif guess > secret:

                print(Fore.YELLOW + "\n📈 Too High!")

                difference = guess - secret

                if difference <= 5:
                    print(Fore.GREEN + "🔥 Very Close!")

            else:

                print(Fore.GREEN + "\n🎉 CONGRATULATIONS!")
                print(Fore.WHITE + f"Correct Number : {secret}")
                print(Fore.CYAN + f"Attempts Used : {attempts}")

                performance(max_attempts, attempts)

                return

        except ValueError:

            print(Fore.RED + "\nPlease Enter Numbers Only!")

        pause()

    header()

    print(Fore.RED + "💀 GAME OVER")
    print(Fore.YELLOW + f"The Correct Number was : {secret}")

    pause()


# ===========================
# Program Starts Here
# ===========================

while True:

    play()

    header()

    again = input(Fore.GREEN + "Play Again? (Y/N): ").strip().lower()

    if again != "y":

        header()

        print(Fore.CYAN + "Thank You For Playing ❤️")
        print(Fore.YELLOW + "Have a Nice Day!")

        break