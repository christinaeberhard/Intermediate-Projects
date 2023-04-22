from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_input.insert(0, password)
    pyperclip.copy(password)    # copying the generated password, so the user can paste it directly

""" saving the password in a file, informing the user and deleting the entries 
in the input fields if the saving was successful """
def save_password():

    website = website_input.get()
    email = mail_input.get()
    password = pw_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't empty field left.")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("passwords.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            pw_input.delete(0, END)


# finding passwords
def find_password():
    website = website_input.get()
    with open("passwords.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")


# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=20)
website_input.grid(column=1, row=1)
website_input.focus()   # sets the cursor in this entry field when launching the app

mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)
mail_input = Entry(width=35)
mail_input.grid(column=1, row=2, columnspan=2)
"""sets the mail address displayed in the beginning of the field when launching th app"""
mail_input.insert(0, "helloworld@gmail.com")

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)
pw_input = Entry(width=20)
pw_input.grid(column=1, row=3)

search_button = Button(text="Search", width=10, command=save_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", width=10, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()