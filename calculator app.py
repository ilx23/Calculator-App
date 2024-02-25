# Importing necessary modules
from tkinter import *
from tkinter import messagebox

# Creating the main application window
app = Tk()
app.title("Calculator App")  # Setting the title of the application window
app.geometry("500x300")  # Setting the size of the application window


# Function to display the result of the calculation
def show_result():
    entry_value = calc_entry.get()  # Getting the value from the entry widget
    # Checking if the entry is empty
    if not entry_value:
        messagebox.showerror("Error", "The box is Empty!")  # Displaying an error message if the entry is empty
    else:
        try:
            # Evaluating the expression and displaying the result
            result = eval(entry_value)
            calc_entry.delete(0, END)  # Clearing the entry widget
            calc_entry.insert(0, result)  # Inserting the result into the entry widget
        except NameError:
            # Displaying an error message if the entry contains non-numeric characters
            messagebox.showerror("Error", "Please enter numbers not words!")
            calc_entry.delete(0, END)  # Clearing the entry widget


# Creating the entry widget for the calculator
calc_entry = Entry(width=53, font="aria", relief=GROOVE, borderwidth=5)
calc_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Creating and positioning the number buttons
# First row
seven_button = Button(text="7", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "7"))
seven_button.grid(row=1, column=0)
eight_button = Button(text="8", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "8"))
eight_button.grid(row=1, column=1)
nine_button = Button(text="9", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "9"))
nine_button.grid(row=1, column=2)
division_button = Button(text="/", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "/"))
division_button.grid(row=1, column=3)
# Second row
four_button = Button(text="4", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "4"))
four_button.grid(row=2, column=0)
five_button = Button(text="5", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "5"))
five_button.grid(row=2, column=1)
six_button = Button(text="6", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "6"))
six_button.grid(row=2, column=2)
multiplication_button = Button(text="*", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "*"))
multiplication_button.grid(row=2, column=3)
# Third row
one_button = Button(text="1", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "1"))
one_button.grid(row=3, column=0)
two_button = Button(text="2", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "2"))
two_button.grid(row=3, column=1)
three_button = Button(text="3", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "3"))
three_button.grid(row=3, column=2)
minus_button = Button(text="-", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "-"))
minus_button.grid(row=3, column=3)
# Fourth row
zero_button = Button(text="0", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "0"))
zero_button.grid(row=4, column=0)
# Creating and positioning the "ce" (clear entry) button
ce_button = Button(text="ce", font=("aria", 20), width=5, command=lambda: calc_entry.delete(0, END))
ce_button.grid(row=4, column=1)
# Creating and positioning the "=" (equal) button
equal_button = Button(text="=", font=("aria", 20), width=5, command=show_result)
equal_button.grid(row=4, column=2)
# Creating and positioning the "+" (addition) button
plus_button = Button(text="+", font=("aria", 20), width=5, command=lambda: calc_entry.insert(END, "+"))
plus_button.grid(row=4, column=3)

# Creating and positioning the developer label
developer_label = Label(text="Made by Ilia keshavarz", font=("aria", 9, 'bold'), fg="#212121")
developer_label.grid(row=5, column=0, columnspan=4, pady=20)

# Starting the Tkinter event loop
app.mainloop()

app.mainloop()
