from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please make sure you haven't empty field left.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                               f"\nPassword: {password} \nDo you want to save this?")
        if is_ok:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                pw_input.delete(0, END)

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
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
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

generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()