# Library Page


import os 
import random
import csv

class Library:
    def __init__(self,member_id):
        self.member_id = member_id

    def main(self):
        os.system("cls")
        print("**************************************")
        print("*           Welcome to the           *")
        print("*               Library              *")
        print("*                                    *")
        print("**************************************")
        print("Select either 1,2,3 or 4:")
        print("1. Borrow book")
        print("2. Return book")
        print("3. Show books you borrowed")
        print("4. Show all books in library")
        choice = input()
        if choice == "1":
            self.borrow_book()
        if choice == "2":
            self.return_book()
        if choice == "3":
            self.show_books_for_user()
        if choice == "4":
            self.show_all_books()
        else:
            print("Incorrect input. Please try again.")
            self.main()
    
    def show_all_books(self):
        os.system("cls")   
        main_csv_path = "./Database/main.csv"
        with open(main_csv_path, "r") as f:
            reader = csv.reader(f)
            main_rows = list(reader)
            for row in main_rows[1:]:
                print(f"""
                ________________________________
                    Title: {row[0]}
                    Author: {row[1]}
                    Total copies: {row[2]}
                    Available copies: {row[3]}
                    IBSN: {row[4]}
                        """)
            input("Press enter to return to homepage")
            self.main()

    def show_books_for_user(self):
        os.system("cls")
        mylist = []
        book_name_list = []
        db_csv_path = "./Database/db.csv"
        main_csv_path = "./Database/main.csv"
        with open(db_csv_path, mode="r") as file:
            reader = csv.reader(file)
            db_rows = list(reader)
            member_found = False  
            for member_row in db_rows[1:]:  # Skip the header row
                    if member_row[2] == self.member_id:
                            member_found = True
                            current_borrowed = member_row[4]
        
                            for i in current_borrowed.split(","):
                                mylist.append(i)
                            

                            with open(main_csv_path, "r") as f:
                                reader = csv.reader(f)
                                main_csv_rows = list(reader)
                                for isbn_row in main_csv_rows[1:]:
                                    for i in mylist:
                                        if i == isbn_row[4]:
                                            book_name_list.append(isbn_row[0])
                                            
             
            currently_borrowed_books = ",".join(book_name_list)   
            if len(book_name_list) > 0:  
                print(F"You currently have: {currently_borrowed_books} borrowed")   
                input("Press enter to go back to home page")        
                self.main()         
            else:
                print("You currently have no books borrowed.")      
                input("Press enter to return to homepage.")  
                self.main()                 

    def borrow_book(self):

        os.system("cls")

        repeat = False
        while not repeat:
            main_csv_path = './Database/main.csv'
            db_csv_path = './Database/db.csv'

            search_isbn = input("What is the ISBN of the book you would like to borrow? ")

            # Read the main.csv to find the book
            with open(main_csv_path, mode='r') as file:
                reader = csv.reader(file)
                main_rows = list(reader)

            book_found = False
            for book_row in main_rows[1:]:  # Skip the header row
                if book_row[4] == search_isbn:  # Check if the ISBN matches
                    book_found = True
                    print(f"Would you like to borrow the book '{book_row[0]}' by author '{book_row[1]}', y or n?")
                    correct_book = input()
                    if correct_book.lower() == "y":
                        available_copies = int(book_row[3])
                        if available_copies > 0:  
                            book_row[3] = str(available_copies - 1)
                            

                            # Read db.csv to update the borrowed_books
                            with open(db_csv_path, mode='r') as db_file:
                                db_reader = csv.reader(db_file)
                                db_rows = list(db_reader)

                            member_found = False  
                            for member_row in db_rows[1:]:  # Skip the header row
                                if member_row[2] == self.member_id:
                                    member_found = True
                                    current_borrowed = member_row[4]  # Get the current borrowed_books
                                    if search_isbn in current_borrowed:
                                        print("Already borrowed book.")
                                        input("Press enter to return to homepage.")
                                        self.main()
                                    else:
                                        if current_borrowed:  # If there are already borrowed books
                                            # Append the new ISBN, separating with a comma
                                            updated_borrowed = current_borrowed + ',' + search_isbn
                                        else:
                                            updated_borrowed = search_isbn  # If no books borrowed yet
                                    
                                        # Update the borrowed_books field
                                        member_row[4] = updated_borrowed
                                        print(f"Successfully borrowed {book_row[0]}")
                                        break

                            # If member not found, inform the user
                            if not member_found:
                                print("Member ID not found. Please check the ID and try again.")
                            else:
                                # Write the updated main.csv back
                                with open(main_csv_path, mode='w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(main_rows)

                                # Write the updated db.csv back
                                with open(db_csv_path, mode='w', newline='') as db_file:
                                    db_writer = csv.writer(db_file)
                                    db_writer.writerows(db_rows)

                                repeat = True
                        else:
                            print("No available copies left for this book.")
                    else:
                        print("Operation canceled. Please try again.")

            if not book_found:
                print("Book with that ISBN not found. Please try again.")
                input("Press enter to return to homepage.")
                self.main()
        
        input("Press enter to return to homepage.")
        self.main()
             
    
    def return_book(self):

        os.system("cls")

        main_csv_path = './Database/main.csv'
        csv_file_path = './Database/db.csv'
        search_isbn = input("Enter the ISBN of the book you would like to return: ")

        with open(main_csv_path, mode='r') as file:
                reader = csv.reader(file)
                main_rows = list(reader)

        book_found = False
        for book_row in main_rows[1:]:  # Skip the header row
                if book_row[4] == search_isbn:  # Check if the ISBN matches
                    book_found = True
                    print(f"Would you like to return the book '{book_row[0]}' by author '{book_row[1]}', y or n?")
                    correct_book = input()
                    if correct_book.lower() == "y":
                        available_copies = int(book_row[3])
                        if available_copies > 0:  
                            book_row[3] = str(available_copies + 1)


        with open(main_csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(main_rows)


        # Read the db.csv file to update the borrowed_books
        with open(csv_file_path, mode='r') as db_file:
            db_reader = csv.reader(db_file)
            db_rows = list(db_reader)


        member_found = False
        for member_row in db_rows[1:]:  # Skip the header row
            if member_row[2] == self.member_id:  # Assuming you have `self.member_id` set somewhere
                member_found = True
                current_borrowed = member_row[4]  # Get the current borrowed_books
                
                if search_isbn in current_borrowed:
                    borrowed_books_list = current_borrowed.split(",")  # Split the books by comma
                    if search_isbn in borrowed_books_list:
                        borrowed_books_list.remove(search_isbn)  # Remove the book from the list
                        print(f"Returning book with ISBN: {search_isbn}")
                    
                    # Join the updated list back into a string
                    updated_borrowed_books = ",".join(borrowed_books_list)
                    member_row[4] = updated_borrowed_books  # Update the CSV row
                else:
                    print(f"ISBN {search_isbn} not found in borrowed books.")
                    input("Press enter to return to homepage.")
                    self.main()

        # If member not found, inform the user
        if not member_found:

            print("Member ID not found. Please check the ID and try again.")

        else:

            # Write the updated rows back to the CSV
            with open(csv_file_path, mode='w', newline='') as db_file:
                db_writer = csv.writer(db_file)
                db_writer.writerows(db_rows)
            print("Borrowed books updated successfully.")
            input("Press enter to return to homepage.")
            self.main()