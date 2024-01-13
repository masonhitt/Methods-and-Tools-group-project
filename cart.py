import sqlite3
import sys
from user import User



class Cart:
    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName

        try:
            self.connection = sqlite3.connect(self.databaseName)
            self.cursor = self.connection.cursor()
        except:
            print("Failed database connection.")
            sys.exit()

    def viewCart(self, userID, inventoryDatabase):
        user = User(self.databaseName)
        if user.getLoggedIn():
            inventory = Inventory(inventoryDatabase)
            inventory.view_inventory()
        else:
            print("User is not logged in.")

    def addToCart(self, userID, ISBN, quantity=1):
        user = User(self.databaseName)
        if user.getLoggedIn():
            inventory = Inventory(self.databaseName)
            inventory.decrease_stock(ISBN, quantity)
            current_userID = user.getUserID()
        else:
            print("User is not logged in.")

    def removeFromCart(self, userID, ISBN):
        user = User(self.databaseName)
        if user.getLoggedIn():
            #
            current_userID = user.getUserID()
        else:
            print("User is not logged in.")

    def checkOut(self, userID):
        user = User(self.databaseName)
        if user.getLoggedIn():
            current_userID = user.getUserID()
        else:
            print("User is not logged in.")