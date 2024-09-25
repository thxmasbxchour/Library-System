# Register Form


import os
import random
import csv
from classes.login_file import Login


class Register:
    def __init__(self):
        pass

    def member_id_gen(self):
        mylist = []
        for i in range(10):
            x = str(random.randint(1,9))
            mylist.append(x)
        
        member_id = "".join(mylist)
        return member_id
        

    def main(self):
            os.system("cls")
            print("**************************************")
            print("*           Welcome to the           *")
            print("*          Registration Form         *")
            print("*                                    *")
            print("**************************************")
            name = input("What's your name? ")
            age = int(input("What's your age? "))
            password = input("What would you like your password to be? ")
            member_id = self.member_id_gen()
                    
            data_to_append = [name,age,member_id,password,None]
            file = open("db.csv", "a", newline="")
            writer = csv.writer(file)
            writer = writer.writerow(data_to_append)
            file.close()

            print("Succesfully created account. Please write the following information down or keep in a safe place AND DO NOT FORGET PASSWORD!")
            print(f"Member ID: {member_id}")
            input("Press enter when you are ready to login")
            L1 = Login()
            L1.main()