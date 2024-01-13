import sqlite3
import sys

class Inventory:

    def __init__(self, database_name="inventory.db", table_name=None):
        self.database_name = database_name
        self.table_name = table_name

        try:
            self.connection = sqlite3.connect(self.database_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Failed database connection: {e}")
            sys.exit()

    def set_database(self, database_name):
        self.database_name = database_name

    def view_inventory(self):
        if not self.database_name or not self.table_name:
            print("Database name or table name not provided.")
            return

        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name}")
            rows = self.cursor.fetchall()

            if not rows:
                print("Inventory is empty.")
            else:
                for row in rows:
                    print(row)

        except sqlite3.Error as e:
            print(f"Error viewing inventory: {e}")

        finally:
            if self.connection:
                self.connection.close()

    def search_inventory(self, title):
        if not self.database_name or not self.table_name:
            print("Database name or table name not provided.")
            return

        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE Title LIKE ?", ('%' + title + '%',))
            rows = self.cursor.fetchall()

            if not rows:
                print("No results found.")
            else:
                for row in rows:
                    print(row)

        except sqlite3.Error as e:
            print(f"Error searching inventory: {e}")

        finally:
            if self.connection:
                self.connection.close()

    def decrease_stock(self, ISBN, quantity=1):
        if not self.database_name or not self.table_name:
            print("Database name or table name not provided.")
            return

        try:
            self.cursor.execute(f"UPDATE {self.table_name} SET Stock = Stock - ? WHERE ISBN = ?", (quantity, ISBN))
            self.connection.commit()

            print(f"Stock for ISBN {ISBN} decreased by {quantity}.")

        except sqlite3.Error as e:
            print(f"Error decreasing stock: {e}")

        finally:
            if self.connection:
                self.connection.close()
