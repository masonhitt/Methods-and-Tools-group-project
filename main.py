import sys
from user import User
from cart import Cart
from inventory import Inventory

def initialMenu():
    user = User()
    cart = Cart(databaseName="methods.db")
    inventory = Inventory(database_name="methods.db", table_name="Inventory")

    while True:
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if initial == "0":
            user.login()

        elif initial == "1":
            user.createAccount()

        elif initial == "2":
            print("Good-bye!")
            break

        else:
            print("That's not a menu option. Please try again.")

        print()

        if user.getLoggedIn():
            mainMenu(user, cart, inventory)

    return user  

def mainMenu(user, cart, inventory):
    while user.getLoggedIn():
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            user.logout()
            print("Successful logout.")

        elif option == "1":
            user.viewAccountInformation()

        elif option == "2":
            inventory.set_database("methods.db")
            inventory.view_inventory()

        elif option == "3":
            cartMenu(cart, user, inventory)

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
            cart.viewCart()


        elif option == "2":
            ISBN = input("Enter ISBN of the book to add: ")
            quantity = int(input("Enter quantity (default is 1): ") or 1)
            cart.addToCart(user, ISBN, quantity)


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
    user = initialMenu()  # Get the user object returned by initialMenu
    inventory = Inventory(database_name="methods.db", table_name="Inventory")
    if user.getLoggedIn():
        mainMenu(user, Cart(), inventory)
    
    inventory.close_connection()    

main()