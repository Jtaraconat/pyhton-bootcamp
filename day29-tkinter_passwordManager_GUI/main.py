from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip 
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) #copy password to clipboard automatically

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_as_file():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data = {website_input: {
        "email": email_input,
        "password" : password_input
    }}

    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Check fields", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            #update old data with new
            data.update(new_data)
            with open ("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#---------------------------FIND PASSWORD-------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Not data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details exist for {website}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#LABELS
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

#ENTRIES
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mail@mail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

#BUTTONS
search_button = Button(text="Search", width=7, command=find_password)
search_button.grid(column=2, row=1)

password_button =  Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data_as_file)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()