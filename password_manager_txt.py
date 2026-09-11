"""
PASSWORD MANAGER PROJECT (TEXT FILE VERSION)
Class 12 CBSE - Computer Science
Stores records as comma-separated lines in a plain text (.txt) file.
Each record is itself a list: [name, email, password]
Functions: CREATE, ADD, DISPLAY, SEARCH, UPDATE, COPY, DELETE
"""

FILENAME = "passwords.txt"

NAME = 0
EMAIL = 1
PASSWORD = 2


# ---------------- helper: load whole list ----------------
def load_records():
    records = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip("\n")
                if line == "":
                    continue
                rec = line.split(",")
                records.append(rec)
    except FileNotFoundError:
        return []
    return records


# ---------------- helper: save whole list ----------------
def save_records(records):
    with open(FILENAME, "w") as f:
        for rec in records:
            f.write(",".join(rec) + "\n")


# ---------------- 1. CREATE ----------------
def create():
    records = []   # write mode - overwrites/erases old records

    while True:
        nme = input("Enter name: ")
        eml = input("Enter email: ")
        pwd = input("Enter password: ")

        rec = [nme, eml, pwd]

        records.append(rec)
        print("Record added successfully.\n")

        more = input("Add more entries? (y/n): ")
        if more.lower() != "y":
            break

    save_records(records)


# ---------------- 1b. ADD ----------------
def add():
    records = load_records()

    while True:
        nme = input("Enter name: ")
        eml = input("Enter email: ")
        pwd = input("Enter password: ")

        rec = [nme, eml, pwd]

        records.append(rec)
        print("Record added successfully.\n")

        more = input("Add more entries? (y/n): ")
        if more.lower() != "y":
            break

    save_records(records)


# ---------------- 2. DISPLAY ----------------
def display():
    records = load_records()

    if not records:
        print("No records to display.\n")
        return

    for rec in records:
        print("Name     :", rec[NAME])
        print("Email    :", rec[EMAIL])
        print("Password :", rec[PASSWORD])
        print("-" * 30)
    print()


# ---------------- 3. SEARCH ----------------
def search():
    records = load_records()

    if not records:
        print("No records found. File does not exist yet.\n")
        return

    target = input("Enter name to search: ")
    found = False

    for rec in records:
        if rec[NAME] == target:
            print("Record found:")
            print("Name     :", rec[NAME])
            print("Email    :", rec[EMAIL])
            print("Password :", rec[PASSWORD])
            found = True

    if not found:
        print("No record found with that name.\n")
    else:
        print()


# ---------------- 4. UPDATE ----------------
def update():
    records = load_records()

    if not records:
        print("No records found. File does not exist yet.\n")
        return

    target = input("Enter name of record to update: ")
    found = False

    for rec in records:
        if rec[NAME] == target:
            found = True
            print("Current password:", rec[PASSWORD])
            new_pwd = input("Enter new password: ")
            rec[PASSWORD] = new_pwd
            print("Record updated.\n")

    if not found:
        print("Record not found.\n")
        return

    save_records(records)


# ---------------- 5. COPY ----------------
def copy_file():
    records = load_records()

    if not records:
        print("No records found. File does not exist yet.\n")
        return

    backup_name = input("Enter name for backup file (e.g. backup.txt): ")

    with open(backup_name, "w") as f2:
        for rec in records:
            f2.write(",".join(rec) + "\n")

    print("Backup copy created as", backup_name, "\n")


# ---------------- 6. DELETE ----------------
def delete():
    records = load_records()

    if not records:
        print("No records found. File does not exist yet.\n")
        return

    target = input("Enter name of record to delete: ")

    new_records = []
    for rec in records:
        if rec[NAME] != target:
            new_records.append(rec)
        else:
            pass

    if len(new_records) == len(records):
        print("Record not found. Nothing deleted.\n")
        return

    save_records(new_records)
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
