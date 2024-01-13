class Cart:

    try:
            connection = sqlite3.connect(self.databaseName)

        except:
            print("Failed database connection.")

            ## exits the program if unsuccessful
            sys.exit()

        ## cursor to send queries through
        cursor = connection.cursor()


    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName

    def viewCart(self, userID, inventoryDatabase):
        user = User(self.databaseName)
        if user.getLoggedIn():
            inventory = Inventory(inventoryDatabase)
            inventory.viewInventory()
        else:
            print("User is not logged in.")

    def addToCart(self, userID, ISBN, quantity=1):
        user = User(self.databaseName)
        if user.getLoggedIn():
            inventory = Inventory(self.databaseName)
            inventory.decreaseStock(ISBN, quantity)
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

