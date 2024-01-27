"""
Terminal application that calculates payment amount per payment period
"""

import locale
from pyfiglet import Figlet

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# WELCOME SCREEN

fig = Figlet(font="isometric1")
print(fig.renderText("LOAN"))

print("WELCOME TO LOAN CALCULATOR.")
print("It's simple. Just follow the prompts!\n")

# VARIABLES

PLAY_AGAIN = True

while PLAY_AGAIN:
    loan_amount = float(input("\nHow much did you borrow?: "))
    interest_rate = float(input("What is your annual interest rate (%)?: "))
    payments_per_year = int(input("How many payments per year?: "))

    # PAYMENT CALCULATION

    payment_amount = loan_amount * ((interest_rate / 100) / payments_per_year)

    # MESSAGE

    print(
        f"\nYou borrowed {locale.currency(loan_amount)} with an interest rate of {interest_rate}%?"
    )
    print(f"With {payments_per_year} payments per year, each payment should be...\n")
    print(f"{locale.currency(payment_amount)}\n")

    replay_choice = input("Try another calculation? Enter Y/N...: ")  # APP REPLAY

    PLAY_AGAIN = bool(replay_choice.upper() == "Y")

print("Thanks for playing! See you again next time!")  # APP END
