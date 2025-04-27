import tkinter as tk

passwords = {}

def mainMenu():
    for widget in root.winfo_children(): # destroys any widget that is currently on the window
        widget.destroy()

    global viewPassButton, addAccButton, searchPassButton # allows to be updated globally

    viewPassButton = tk.Button(root, text="View Accounts", command=viewPass)
    addAccButton = tk.Button(root, text="Add Account", command=addAcc)
    searchPassButton = tk.Button(root, text="Search Passwords", command=searchPass)

    viewPassButton.pack()
    addAccButton.pack()
    searchPassButton.pack()    

def savePass():
    username = userEntry.get()
    password = passEntry.get()
    passwords[username] = password

    mainMenu()

def viewPass():
    viewPassButton.destroy()
    addAccButton.destroy()
    searchPassButton.destroy()

    savedLabel = tk.Label(root, text="Saved Accounts:")
    savedLabel.pack()

    for user, pw in passwords.items():
        accountLabel = tk.Label(root, text=f"Username: {user} \n {pw}")
        accountLabel.pack()
        lineLabel = tk.Label(root, text="------------------")
        lineLabel.pack()

    doneButton = tk.Button(root, text="Done", command=mainMenu)
    doneButton.pack()


def addAcc():
    viewPassButton.destroy()
    addAccButton.destroy()
    searchPassButton.destroy()

    global userEntry, passEntry

    userLabel = tk.Label(root, text="Username:")
    userLabel.pack() # places userLabel onto screen

    userEntry = tk.Entry(root)
    userEntry.pack()

    passTitle = tk.Label(root, text="Password:")
    passTitle.pack()

    passEntry = tk.Entry(root)
    passEntry.pack()

    enterButton = tk.Button(root, text="Enter", command=savePass)
    enterButton.pack()


def searchPass():
    viewPassButton.destroy()
    addAccButton.destroy()
    searchPassButton.destroy()

    searchLabel = tk.Label(root, text="Enter Account Name:")
    searchEntry = tk.Entry(root)

    searchLabel.pack()
    searchEntry.pack()

    def performSearch():
        search = searchEntry.get()

        if search in passwords:
            resultLabel = tk.Label(root, text=f"{search} was found in the system.")
            resultLabel.pack()
        else:
            resultLabel = tk.Label(root, text=f"{search} was not found in the system.")
            resultLabel.pack()
        
        searchButton.destroy()
        doneButton = tk.Button(root, text="Done", command=mainMenu)
        doneButton.pack()

    searchButton = tk.Button(root, text="Search", command=performSearch)
    searchButton.pack()

root = tk.Tk() # creates the UI window
root.title("Password manager") # sets the title as password manager
root.geometry("600x400") # dimension of window

userLabel = tk.Label(root, text="Username:")
userLabel.pack() # places userLabel onto screen

userEntry = tk.Entry(root)
userEntry.pack()

passTitle = tk.Label(root, text="Password:")
passTitle.pack()

passEntry = tk.Entry(root)
passEntry.pack()

enterButton = tk.Button(root, text="Enter", command=savePass)
enterButton.pack()

viewPassButton = tk.Button(root, text="View Accounts", command=viewPass)
addAccButton = tk.Button(root, text="Add Account", command=addAcc)
searchPassButton = tk.Button(root, text="Search Passwords", command=searchPass)

root.mainloop() # starts main loop












# passwords = {}

# usernameInput = input("Enter a username: ")
# passInput = input("Enter a password: ")
# passwords[usernameInput] = passInput


# while True:

#     print("1. Add Password")
#     print("2. View all Passwords")
#     print("3. Search for a Password")
#     print("4. Quit")

#     choice = input("Enter a number 1-4: ")

#     if (choice == "1"):
#         usernameInput = input("Enter a username: ")
#         passInput = input("Enter a Password: ")
#         passwords[usernameInput] = passInput

#     if (choice == "2"):
#         for user, password in passwords.items():
#             print(f"Username: {user} | Password: {password}") # iterates through each user and password in passwords dictionary

#     if (choice == "3"):
#         search = input("Enter password you'd like to search: ")
#         if (search in passwords):
#             print(f"Password for {search}: {passwords[search]}")
#         else:
#             print(f"Password for {search} was not found")

#     if (choice == "4"):
#         break


    