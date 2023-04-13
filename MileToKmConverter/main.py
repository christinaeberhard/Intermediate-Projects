from tkinter import *

# write the logic
def miles_to_km():
    miles = user_input.get()
    km = float(miles) * 1.609
    km_result_label.config(text=km)

# Create the window
window = Tk()
window.title("Miles to Kilometers Converter")
#window.minsize(width=350, height=150)
window.config(padx=30, pady=25)

# Create an Entry/Input
user_input = Entry(width=7)
user_input.grid(column=1, row=0)

# Create the labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)


# Create the button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()