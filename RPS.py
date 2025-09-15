#RPS.py
#Name:
#Date:
#Assignment:
print("Adam McLaughlin \t Fall 2025 \t Lab3")
print("")
import random

def main():
    wins = 0
    ties = 0
    losses = 0

    while True:
        computer = random.choice(["R", "P", "S"])
        player = input("Pick your weapon (R, P, S): ").strip().upper()

        if player not in ["R", "P", "S"]:
            print("Invalid choice. Please choose R, P, or S.")
            continue

        # Show choices
        print(f"Computer chose {'Rock' if computer == 'R' else 'Paper' if computer == 'P' else 'Scissors'}")
        print(f"Player chose {'Rock' if player == 'R' else 'Paper' if player == 'P' else 'Scissors'}")

        # Determine outcome
        if player == computer:
            print("Tie")
            ties += 1
        elif (player == "R" and computer == "S") or \
             (player == "P" and computer == "R") or \
             (player == "S" and computer == "P"):
            print("You Win!")
            wins += 1
        else:
            print("Computer wins.")
            losses += 1

        # Ask to play again
        while True:
            play_again = input("Would you like to play again? (Y/N): ").strip().lower()
            if play_again == "y":
                break
            elif play_again == "n":
                print("\nGame Over!!!")
                print("Wins \t Ties \t Losses")
                print("---- \t ---- \t ------")
                print(f"{wins} \t {ties} \t {losses}")
                return
            else:
                print("Please enter Y or N.")

if __name__ == '__main__':
    main()

