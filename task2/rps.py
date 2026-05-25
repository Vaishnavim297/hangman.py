import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

shapes = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

print("=== Rock Paper Scissors Game ===")

while True:
    try:
        user_choice = int(input("\nEnter 0 for Rock, 1 for Paper, 2 for Scissors: "))

        if user_choice not in [0, 1, 2]:
            print("Invalid choice! Please enter 0, 1, or 2.")
            continue

        computer_choice = random.randint(0, 2)

        print("\nYou chose:")
        print(shapes[user_choice])

        print("Computer chose:")
        print(shapes[computer_choice])

        if user_choice == computer_choice:
            print("It's a Draw!")

        elif (
            (user_choice == 0 and computer_choice == 2) or
            (user_choice == 1 and computer_choice == 0) or
            (user_choice == 2 and computer_choice == 1)
        ):
            print("You Win!")

        else:
            print("You Lose!")

        again = input("\nPlay again? (y/n): ").lower()

        if again != 'y':
            print("Thanks for playing!")
            break

    except ValueError:
        print("Please enter a valid number (0, 1, or 2).")