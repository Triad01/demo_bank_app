#!/usr/bin/python3
import random

customers = []

def open_account():

    customer_name = input("What is your name ? ")

    age = int(input("How old are you ? "))

    # Generate a random 10-digit number
    random_number = random.randrange(10**10, 10**11)

    bvn = random_number

    account_pin = int(input("Create a pin for your transactions "))

    deposit_option = input("Do you want to make an initial Deposit ? Type 'y' or 'n' ").lower()

    if deposit_option == "y":

        amount = int(input("Enter amount "))

    else:
        amount = 0

    customers.append({"Name": customer_name, "Age": age, "BVN": bvn, "Amount": amount, "Pin": account_pin})

    print(customers)

def check_pin(pin):
    if customers["Pin"] == pin:
        return True
    else:
        return False

ussd_code = input("Dial ussd code (*770#)\n")

menu = ["Open Account", "Balance", "Airtime", "Transfer", "Bill Payments", "Fast loan", "SME loan", "Collections", "Next"]

if ussd_code == "*770#":

    print("Alert!!!\nPlease do not disclose your Fidelity Bank Online Banking Password/Token, ATM PIN or BVN to anyone. We will never ask for it.")

    proceed_option = int(input("Enter 1 to Proceed| "))

    if proceed_option == 1:
        
        for i, operation in enumerate(menu):

            print(f"{i + 1}>{operation}")

        menu_choice = int(input("pick option>>> "))

        if menu_choice == 1:

            open_account()

        elif menu_choice == 2:
            
            print("Balance enquiry attracts a service fee of #20")

            entered_pin = int(input("Enter pin "))

            if check_pin(entered_pin):
                print("pin okay")
            else:
                print("pin incorrect")

