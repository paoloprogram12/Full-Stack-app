passwords = {}

usernameInput = input("Enter a username: ")
passInput = input("Enter a password: ")
passwords[usernameInput] = passInput


while True:

    print("1. Add Password")
    print("2. View all Passwords")
    print("3. Search for a Password")
    print("4. Quit")

    choice = input("Enter a number 1-4: ")

    if (choice == "1"):
        usernameInput = input("Enter a username: ")
        passInput = input("Enter a Password: ")
        passwords[usernameInput] = passInput

    if (choice == "2"):
        for user, password in passwords.items():
            print(f"Username: {user} | Password: {password}") # iterates through each user and password in passwords dictionary

    if (choice == "3"):
        search = input("Enter password you'd like to search: ")
        if (search in passwords):
            print(f"Password for {search}: {passwords[search]}")
        else:
            print(f"Password for {search} was not found")

    if (choice == "4"):
        break