from tkinter import *
from tkinter import messagebox
import random
import mysql.connector

database = mysql.connector.connect(host="add your host", user="add your username", passwd="Add your mySQL password",
                                   auth_plugin='mysql_native_password', database="add your db")
cursor = database.cursor()

# Constants
# Add Database

BACKGROUNDCOLOR = "#020b0d"
CANVASCOLOR = "#000303"


# Functionality
def addToDB():
    if len(websiteEntry.get()) == 0 or len(passwordEntry.get()) == 0 or len(usernameEntry.get()) == 0:
        return messagebox.showinfo(title="error", message="Please don't leave any fields blank")
    isTrue = messagebox.askokcancel(title=websiteEntry.get(),
                                    message=f"Email/Username: {usernameEntry}\n Are you sure you want to store your information?")
    if (isTrue):
        website = websiteEntry.get()
        username = usernameEntry.get()
        password = passwordEntry.get()
        tuplet = (website, username, password)
        sqlformula = "INSERT INTO info (website, username, password) VALUES (%s, %s, %s)"
        cursor.execute(sqlformula, tuplet)
        database.commit()
        websiteEntry.delete(0, END)
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)


def showAllPasswords():
    cursor.execute("SELECT * FROM info")
    allPasswords = cursor.fetchall()
    passTuples = []
    passMessage = []
    count = 1
    for row in allPasswords:
        passTuples.append(row)
    for i in range(0, len(passTuples)):
        newRow = ""
        for j in range(0, 3):
            if j == 0:
                newRow = str(count) + " "
                count += 1
            newRow = newRow + passTuples[i][j] + " "
        passMessage.append(newRow)
    print(passMessage)
    newCanvas.itemconfig(fullPassText, text="Please Close After Viewing!!")
    dbInitial = Label(root, text="Website, Username, Password")
    dbInitial.grid(row=9, column=1)
    for i in range(0, len(passMessage)):
        dbPassword = Label(root, text=passMessage[i], bg="black", fg="white")
        dbPassword.grid(column=1, row=(10 + i))


def randomPassword():
    passwordEntry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    new_List = []
    for i in range(0, random.randint(4, 7)):
        new_List.append(letters[random.randint(0, len(letters) - 1)])
    for i in range(0, random.randint(1, 4)):
        new_List.append(numbers[random.randint(0, len(numbers) - 1)])
    for i in range(0, random.randint(1, 5)):
        new_List.append(symbols[random.randint(0, len(symbols) - 1)])
    random.shuffle(new_List)
    newPassword = ("".join(new_List))
    passwordEntry.insert(0, newPassword)


# Root
root = Tk()
root.title("Welcome to Lock Up")
root.config(padx=50, pady=50, bg=BACKGROUNDCOLOR)

# Logo
canvas = Canvas(root, width=300, height=370, highlightthickness=0)
logo = PhotoImage(file="lock-img copy.png")
canvas.create_image(154, 180, image=logo)
canvas.grid(row=0, column=1)
newCanvas = Canvas(root, width=300, height=50, highlightthickness=0)
fullPassText = newCanvas.create_text(156, 25, text="Passwords Show Up Here", font=("Georgia", 15))
newCanvas.grid(row=8, column=1)

# Labels
websiteLabel = Label(root, text="Website", bg=BACKGROUNDCOLOR, fg="white")
websiteLabel.grid(column=0, row=1)
usernameLabel = Label(root, text="Email/Username", bg=BACKGROUNDCOLOR, fg="white")
usernameLabel.grid(column=0, row=2)
passwordLabel = Label(root, text="Password", bg=BACKGROUNDCOLOR, fg="white")
passwordLabel.grid(column=0, row=3)

# Entries
websiteEntry = Entry(root, width=35, bg="black", fg="white")
websiteEntry.focus()
websiteEntry.grid(row=1, column=1, columnspan=2, sticky=W, )
usernameEntry = Entry(root, width=35, bg="black", fg="white")
usernameEntry.grid(row=2, column=1, columnspan=2, sticky=W)
passwordEntry = Entry(width=20, bg="black", fg="white")
passwordEntry.grid(row=3, column=1, sticky=W)

# Buttons
addToDataBase = Button(text="Add", width=35, command=addToDB)
addToDataBase.grid(row=4, column=1, columnspan=2, sticky=W)
showPasswords = Button(text="Show All", width=35, command=showAllPasswords)
showPasswords.grid(row=5, column=1, columnspan=2, sticky=W)
randomPassword = Button(text="Password Generator", command=randomPassword)
randomPassword.grid(row=3, column=1, sticky=E, columnspan=2)

root.mainloop()