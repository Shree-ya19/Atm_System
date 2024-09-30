import os
import time #To use functions related to time, such as pausing your program for a few seconds or getting the current time, you need to first import the time module in Python.
clear = lambda :os.system("clear") #shortcut way of making a small function in Python that clears the terminal screen.

def atm_system():
    balance=50000
    print("Insert Atm")
    bank_code=4949

    atm_pin= int(input("Enter pin: "))
    if atm_pin == bank_code:
        while True:
            print('''
            1 : Balance Inquiry
            2 : Deposit
            3 : Withdraw
            4 : Exit''')

            option=int(input("Choose Option : "))
            if option ==1:
                print(f"Your current balance is Rs.{balance}/-")

            elif option ==2:
                deposit_amount=int(input("Enter Deposit Amount: "))
                print(f"Your deposited amount is Rs.{deposit_amount}/-")

                balance= balance+deposit_amount
                print(f"Your total balance is Rs.{balance}/-")
                time.sleep(3)#after showing the deposit amount the screen will be clear in 3 sec
                clear()
                break

            elif option==3:
                withdraw_amount = int(input("Enter the withdraw amount:"))

                if withdraw_amount > balance:
                   print("Sorry....! Insufficient Balance")

                elif withdraw_amount < 499:
                   print("Plesase enter appropriate amount.....sorry try again")

                else:
                   print(f'Amount Rs. {withdraw_amount} is withdraw sucessfully/-')

                   balance = balance - withdraw_amount
                   print(f"Your remaining balance is Rs. {balance}")
                   time.sleep(3)
                   clear()
                   break

            elif option == 4:
               print("Thank you and visit again.....!")
               break

            else:
             print("Please choose correct option")
            break


    else:
         print ("Incorrect PIN")

atm_system()