import tkinter as t

window = t.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Creating a Label
label = t.Label(text="Hello world", font=("Arial", 24, "bold"))
label.pack()        # is packing the label on the screen


# Create a Button & let the label change to the input text when the button is clicked
def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    label.config(text=new_text)


button = t.Button(text="Click me!", command=button_clicked)
button.pack()


# Create a Entry/Input
input = t.Entry(width=10)
input.pack()

window.mainloop()