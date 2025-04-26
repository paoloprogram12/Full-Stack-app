import tkinter as tk

passwords = {}

def savePass():
    username = userEntry.get()
    password = passEntry.get()
    passwords[username] = password
    print("saved.")

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


    