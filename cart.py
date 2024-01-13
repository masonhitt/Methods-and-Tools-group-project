import sqlite3
import sys
from user import User
from inventory import Inventory

class Cart:
    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        self.user = None
        self.inventory = Inventory(database_name=databaseName, table_name="Inventory")

        try:
            self.connection = sqlite3.connect(self.databaseName)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Failed database connection: {e}")
            sys.exit()

    def viewCart(self):
        if self.user and self.user.getLoggedIn():
            self.inventory.open_connection()
            self.inventory.view_inventory()
            self.inventory.close_connection()
        else:
            print("User is not logged in.")

    def addToCart(self, user, ISBN, quantity=1):
        if user.getLoggedIn():
            inventory = Inventory(database_name="methods.db", table_name="Inventory") 
            inventory.decrease_stock(ISBN, quantity)
            current_userID = user.getUserID()
        else:
             print("User is not logged in.")

    def removeFromCart(self, userID, ISBN):
        if self.user and self.user.getLoggedIn():
            current_userID = self.user.getUserID()
        else:
            print("User is not logged in.")

    def checkOut(self, userID):
        if self.user and self.user.getLoggedIn():
            current_userID = self.user.getUserID()
        else:
            print("User is not logged in.")
