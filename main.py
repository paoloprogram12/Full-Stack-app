import tkinter as tk

passwords = {}

def mainMenu():
    for widget in root.winfo_children(): # destroys any widget that is currently on the window
        widget.destroy()

    global viewPassButton, addAccButton, searchPassButton, deleteAccButton # allows to be updated globally

    viewPassButton = tk.Button(root, text="View Accounts", command=viewPass)
    addAccButton = tk.Button(root, text="Add Account", command=addAcc)
    searchPassButton = tk.Button(root, text="Search Passwords", command=searchPass)
    deleteAccButton = tk.Button(root, text="Delete Account", command=deleteAcc)

    viewPassButton.pack()
    addAccButton.pack()
    searchPassButton.pack()    
    deleteAccButton.pack()


def savePass():
    username = userEntry.get()
    password = passEntry.get()
    passwords[username] = password


    mainMenu()

def viewPass():
    viewPassButton.destroy()
    addAccButton.destroy()
    searchPassButton.destroy()
    deleteAccButton.destroy()

    savedLabel = tk.Label(root, text="Saved Accounts:")
    savedLabel.pack()

    for user, pw in passwords.items():
        accountLabel = tk.Label(root, text=f"Username: {user} \n {pw}")
        accountLabel.pack()
        lineLabel = tk.Label(root, text="------------------")
        lineLabel.pack()

    doneButton = tk.Button(root, text="Done", command=mainMenu)
    doneButton.pack()

def deleteAction():
    for user, pw in passwords.items():
        accountButton.destroy()
    cancelButton.destroy()

def deleteAcc():
    viewPassButton.destroy()
    addAccButton.destroy()
    deleteAccButton.destroy()
    searchPassButton.destroy()

    global accountButton, cancelButton

    if len(passwords) == 1:
        noDeleteLabel = tk.Label(root, text="Unable to delete account")
        noDeleteLabel.pack()
        noDeleteButton = tk.Button(root, text="Done", command=mainMenu)
        noDeleteButton.pack()
    else:
        for user, pw in passwords.items():
            accountButton = tk.Button(root, text=f"{user}", command=deleteAction)
            accountButton.pack()

        cancelButton = tk.Button(root, text="Cancel", command=mainMenu)
        cancelButton.pack()


def addAcc():
    viewPassButton.destroy()
    addAccButton.destroy()
    searchPassButton.destroy()
    deleteAccButton.destroy()

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
    deleteAccButton.destroy()


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
deleteAccButton = tk.Button(root, text="Delete Account", command=deleteAcc)

root.mainloop() # starts main loop


    