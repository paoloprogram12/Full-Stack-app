import tkinter as tk

passwords = {}

def mainMenu():
    for widget in root.winfo_children(): # destroys any widget that is currently on the window
        widget.destroy()

    global viewPassButton, addAccButton, searchPassButton

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

def searchPass():
    viewPassButton.destroy()
    addAccButton.destroy()
    searchPassButton.destroy()

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