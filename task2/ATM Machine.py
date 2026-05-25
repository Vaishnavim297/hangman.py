balance =7000
pin = "2299"


def check_balance():
    print("Current Balance: ₹", balance)


def deposit_money():
    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully.")
        print("Updated Balance: ₹", balance)
    else:
        print("Invalid deposit amount!")


def withdraw_money():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid withdrawal amount!")

    elif amount > balance:
        print("Insufficient Balance!")

    else:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")
        print("Remaining Balance: ₹", balance)


def change_pin():
    global pin

    old_pin = input("Enter current PIN: ")

    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        pin = new_pin
        print("PIN changed successfully.")
    else:
        print("Incorrect PIN!")


while True:

    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        change_pin()

    elif choice == "5":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.")