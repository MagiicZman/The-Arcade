import sys
from rps8_arcade_copy import rps
from guess_number import guess_number


def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            # On second runs it says "Welcome back to"
            print(f"\n{name}, \nWelcome back to the Arcade 🕹️  menu.")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess The Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice.lower() not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="An Arcade Game."
    )

    parser.add_argument(
        "-n", "--name", metavar='name',
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    # Note on first run it says "Welcome to"
    print(f"\n{args.name}, \nWelcome To The Arcade 🕹️")

    play_game(args.name)

# python3 arcade.py -n "Zion"
# python3 arcade.py --name "Zion" also works exactly the same
