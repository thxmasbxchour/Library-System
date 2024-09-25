# Login FOrm


import os
import random 
import csv
from classes.library_file import Library

class Login:
    def __init__(self):
        self.member_id = None
    
    def main(self):

        incorrect_info = False
        while incorrect_info == False:
            os.system("cls")
            csv_file_path = "./Database/db.csv"
            print("**************************************")
            print("*           Welcome to the           *")
            print("*             Login Form             *")
            print("*                                    *")
            print("**************************************")
            self.member_id = input("What is your member ID? ")
            password = input("What is your password? ")

            with open(csv_file_path, mode='r') as file:
                    reader = csv.reader(file)
                    rows = list(reader) 

            logged_in = False

            for row in rows:
                if self.member_id == row[2] and password == row[3]:
                    print("Logged in")
                    logged_in = True
                    incorrect_info = True
                    Library1 = Library(self.member_id)
                    Library1.main()
                    break
                    
            if not logged_in:
                print("Incorrect Information")
                input("Press enter to try again.")