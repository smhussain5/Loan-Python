from pyfiglet import Figlet
import locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# WELCOME SCREEN

fig = Figlet(font="isometric1")
print(fig.renderText("LOAN"))

print("WELCOME TO LOAN CALCULATOR.")
print("It's simple. Just follow the prompts!\n")

# VARIABLES
play_again = True

while play_again:
    loan_amount = float(input("\nHow much did you borrow?: "))
    interest_rate = float(input("What is your annual interest rate (%)?: "))
    payments_per_year = int(input("How many payments per year?: "))

    # PAYMENT CALCULATION

    payment_amount = loan_amount * ((interest_rate / 100) / payments_per_year)

    # MESSAGE

    print(f"\nSo you borrowed {locale.currency(loan_amount)} with an annual interest rate of {interest_rate}%?")
    print(f"With {payments_per_year} payments per year, each payment should be...\n")
    print(f"{locale.currency(payment_amount)}\n")

    replay_choice = input("Try another calculation? Enter Y/N...: ")  # APP REPLAY

    if replay_choice.upper() == "Y":
        play_again = True
    else:
        play_again = False

print("Thanks for playing! See you again next time!")  # APP END
