from tkinter import *

# Create a new window
window = Tk()
window.title("Hello world!")
window.minsize(width=500, height=500)

# Creating a Label
label = Label(text="Hello world", font=("Arial", 24, "bold"))
label.pack()        # is packing the label on the screen


# Create a Button & let the label change to the input text when the button is clicked
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    label.config(text=new_text)


button = Button(text="Click me!", command=button_clicked)
button.pack()


# Create a Entry/Input
input = Entry(width=10)
input.pack()

# Create a Textbox and put cursor in the box
text = Text(height=5, width=30)
text.focus()
# adding some starting text
text.insert(END, "Hello, Hello, Hello world!")
# get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Create a Spinbox
def spinbox_used():
    # get the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Create a scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Create a checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Create a radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Create a Listbox
def listbox_used(event):
    # get current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()