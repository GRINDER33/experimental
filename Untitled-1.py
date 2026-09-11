"""
PASSWORD MANAGER PROJECT
Class 12 CBSE - Computer Science
Uses pickle module to store records in a binary (.dat) file.
Each record is a dictionary with keys: name, email, password
Functions: CREATE, DISPLAY, SEARCH, UPDATE, COPY, DELETE
"""

import pickle

FILENAME = "passwords.dat"


# ---------------- 1. CREATE ----------------
def create():
    with open(FILENAME, "ab") as f:   # append binary - so old records are not erased

        while True:
            nme = input("Enter name: ")
            eml = input("Enter email: ")
            pwd = input("Enter password: ")

            l = {}
            l["name"] = nme
            l["email"] = eml
            l["password"] = pwd

            pickle.dump(l, f)
            print("Record added successfully.\n")

            more = input("Add more entries? (y/n): ")
            if more.lower() != "y":
                break


# ---------------- 1b. ADD ----------------
def add():
    with open(FILENAME, "ab") as f:   # append binary - so old records are not erased

        while True:
            nme = input("Enter name: ")
            eml = input("Enter email: ")
            pwd = input("Enter password: ")

            rec = {}
            rec["name"] = nme
            rec["email"] = eml
            rec["password"] = pwd

            pickle.dump(rec, f)
            print("Record added successfully.\n")

            more = input("Add more entries? (y/n): ")
            if more.lower() != "y":
                break


# ---------------- 2. DISPLAY ----------------
def display():
    try:
        with open(FILENAME, "rb") as f:
    
            found = False
            while True:
                try:
                    l = pickle.load(f)
                    print("Name     :", l["name"])
                    print("Email    :", l["email"])
                    print("Password :", l["password"])
                    print("-" * 30)
                    found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
        return


    if not found:
        print("No records to display.\n")
    else:
        print()


# ---------------- 3. SEARCH ----------------
def search():
    try:
        with open(FILENAME, "rb") as f:

            target = input("Enter name to search: ")
            found = False

            while True:
                try:
                    l = pickle.load(f)
                    if l["name"] == target:
                        print("Record found:")
                        print("Name     :", l["name"])
                        print("Email    :", l["email"])
                        print("Password :", l["password"])
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
        return


    if not found:
        print("No record found with that name.\n")
    else:
        print()


# ---------------- 4. UPDATE ----------------
def update():
    try:
        with open(FILENAME, "rb") as f:

            records = []
            while True:
                try:
                    records.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
        return
    

    target = input("Enter name of record to update: ")
    found = False

    for rec in records:
        if rec["name"] == target:
            found = True
            print("Current password:", rec["password"])
            new_pwd = input("Enter new password: ")
            rec["password"] = new_pwd
            print("Record updated.\n")

    if not found:
        print("Record not found.\n")
        return

    # rewrite entire file with updated list
    with open(FILENAME, "wb") as f:
        for rec in records:
            pickle.dump(rec, f)
    


# ---------------- 5. COPY ----------------
def copy_file():
    try:
        with open(FILENAME, "rb") as f:

            records = []
            while True:
                try:
                    records.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
        return

    backup_name = input("Enter name for backup file (e.g. backup.dat): ")

    with open(backup_name, "wb") as f2:
        for rec in records:
            pickle.dump(rec, f2)

    print("Backup copy created as", backup_name, "\n")


# ---------------- 6. DELETE ----------------
def delete():
    try:
        with open(FILENAME, "rb") as f:

            records = []
            while True:
                try:
                    records.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
        return

    target = input("Enter name of record to delete: ")

    # new_records = [rec for rec in records if rec["name"] != target]
    new_records = []
    for rec in records:
        if rec["name"] != target:
            new_records.append(rec)
        else:
            pass

    if len(new_records) == len(records):
        print("Record not found. Nothing deleted.\n")
        return

    with open(FILENAME, "wb") as f:
        for rec in new_records:
            pickle.dump(rec, f)

    print("Record deleted successfully.\n")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("========== PASSWORD MANAGER ==========")
        print("1. CREATE")
        print("2. ADD")
        print("3. DISPLAY")
        print("4. SEARCH")
        print("5. UPDATE")
        print("6. COPY")
        print("7. DELETE")
        print("8. EXIT")

        ch = input("Enter your choice (1-8): ")

        if ch == "1":
            create()
        elif ch == "2":
            add()
        elif ch == "3":
            display()
        elif ch == "4":
            search()
        elif ch == "5":
            update()
        elif ch == "6":
            copy_file()
        elif ch == "7":
            delete()
        elif ch == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()