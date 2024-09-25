### Library System - Starter page

import csv
import random
import os
from classes.library_file import Library    
from classes.login_file import Login
from classes.register_file import Register

            

class HomePage:
    def __init__(self):
        pass

    def main(self):
        print("**************************************")
        print("*            Welcome to the          *")
        print("*          Library Management        *")
        print("*              System                *")
        print("**************************************")
        print("\nWhat would you like to do?")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input()
        if choice == "1":
            L1 = Login()
            L1.main()
        if choice == "2":
            M1 = Register()
            M1.main()
        if choice == "3":
            print("No worries, Thanks for using our library system!")


H = HomePage()
H.main()