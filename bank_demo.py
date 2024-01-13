#!/usr/bin/python3
import ascii
import os

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter deposit amount "))

        self.balance += amount
        print(f"Successfully deposited #{amount} to your account ✅")
        print(f"Your balance is #{self.balance}")

    def withdraw(self):
        amount = int(input("Enter withdrawal amount "))

        if amount > self.balance:

            print("Insufficient balance! ❌")
        else:

            self.balance = self.balance - amount

            print(f"Withdrawal of #{amount} successful ✅")
            print(f"Your balance is #{self.balance}")

    def check_balance(self):

        print (f"{self.name}'s balance is #{self.balance}")

    def __str__(self):

        return f"Accound Holder Name - {self.name} \n Balance - #{self.balance}"

    @staticmethod
    def display_welcome_message():
        print("ALERT!!!\nPlease do not disclose your fidelity Bank Online Banking Password/Token, ATM PIN or BVN to anyone.\nWe will never ask for it")
        proceed_code = int(input("Enter 1 to proceed: "))
        return proceed_code

    @staticmethod
    def screen_action(msg = "bye"):
        if msg == "print":
            os.system("clear")
            print(ascii.art)
        elif msg == "bye":
            print("Thanks for banking with us!")
            os.system("clear")

def main():
    ussd_code = input("Enter ussd code: ")
    if ussd_code == "*770#":
        proceed_code = BankAccount.display_welcome_message()
        if proceed_code == 1:
            BankAccount.screen_action("print")
            isActive = True

            print("Welcome to Fidelity instant banking... =======================================================")
            user_name = input("Enter your name ")
            """creating an instance object of the BankAccount class"""
            user = BankAccount(user_name)
            while isActive:
                actions = ["Deposit", "withdrawal", "check balance"]
                for i, action in enumerate(actions):
                    print("{} {}".format(i + 1, action))

                option = int(input("Please select an operation: "))

                if option == 1:
                    BankAccount.screen_action("print")
                    user.deposit()

                    choice = input("Do you want to perform other transactions ? yes/no ").lower()


                    if choice != "yes":
                        BankAccount.screen_action()
                        isActive = False
                    else:

                        BankAccount.screen_action("print")

                elif option == 2:
                    BankAccount.screen_action("print")
                    user.withdraw()

                    choice = input("Do you want to perform other transactions ? yes/no ").lower()

                    if choice != "yes":
                        BankAccount.screen_action()
                        isActive = False
                    else:
                        BankAccount.screen_action("print")

                elif option == 3:
                    BankAccount.screen_action("print")
                    user.check_balance()

                    choice = input("Do you want to perform other transactions ? yes/no ").lower()

                    if choice != "yes":
                        BankAccount.screen_action()
                        isActive = False

                else:
                    BankAccount.screen_action("print")
                    print("Please enter a valid input!")

main()
