from user import *
from cart import *
from inventory import *


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory)


## incomplete main menu...
def mainMenu(user, cart, inventory):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        option = input("Enter your menu choice: ")
        print()

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

def cartMenu(cart, user, inventory):
    while True:
        print("\nCart Menu:")
        print("0. Go Back")
        print("1. View Cart")
        print("2. Add Items to Cart")
        print("3. Remove an Item from Cart")
        print("4. Check Out")
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            break

        elif option == "1":
            cart.viewCart(user.getUserID(), inventory.getDatabaseName())

        elif option == "2":
            ISBN = input("Enter ISBN of the book to add: ")
            quantity = int(input("Enter quantity (default is 1): ") or 1)
            cart.addToCart(user.getUserID(), ISBN, quantity)

        elif option == "3":
            ISBN = input("Enter ISBN of the book to remove: ")
            cart.removeFromCart(user.getUserID(), ISBN)

        elif option == "4":
            cart.checkOut(user.getUserID())
            print("Items checked out successfully.")

        else:
            print("That's not a menu option. Please try again.")
        print()


def main():
    print("Welcome to the online bookstore!\n")

    

    initialMenu()

main()