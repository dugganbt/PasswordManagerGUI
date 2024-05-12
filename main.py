from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LABEL_FONT = ("Helvetica", 12)

"""
This is an example project for a password generator GUI. IT IS NOT INTENDED FOR ACTUAL USE AND IS NOT SAFE FOR 
STORING PASSWORDS, as they are not encrypted and stored merely in a text file. 

From the course: 100 Days of Code by Dr. Angela Yu
"""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  password_list +=[random.choice(letters) for char in range(nr_letters)]
  password_list +=[random.choice(symbols) for char in range(nr_symbols)]
  password_list +=[random.choice(numbers) for char in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)
  password_field.insert(0,password)

  # copy generated password directly to clipboard
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_login():
    # Get current values in the field
    website_entry = website_entry_field.get()
    email_entry = email_user_field.get()
    password_entry = password_field.get()

    # check if all fields have an entry
    if website_entry=="" or email_entry=="" or password_entry=="":
        messagebox.showwarning(message="Oops", detail="Please don't leave any fields empty!")

    else: # If all fields have a value, then ask to confirm

        # Open message box to ask user to confirm
        confirmed_save = messagebox.askokcancel(title=website_entry, message=f"These are the details entered: \n Email: {email_entry}"
                                                                f"\npassword: {password_entry} \nIs it ok to save? ")

        if confirmed_save:
            # save values into the txt file
            with open("data.txt", "a") as file:
                file.write(f"{website_entry} | {email_entry} | {password_entry} \n")
                website_entry_field.delete(0, END)
                password_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Initialize window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas of logo
canvas = Canvas(width=200, height=200)
# Photo Image creation to convert file for the canvas
img = PhotoImage(file="logo.png")
# Placing the image onto the canvas
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Website label and entry field
website_label = Label(text="Website:", font=LABEL_FONT)
website_label.grid(column=0, row=1)

website_entry_field = Entry(width=35)
website_entry_field.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry_field.focus()

# Email/Username label and entry field
email_user_label = Label(text="Email/Username:", font=LABEL_FONT)
email_user_label.grid(column=0, row=2)

email_user_field = Entry()
email_user_field.grid(column=1, row=2, columnspan=2, sticky="ew")
email_user_field.insert(END, "youremail@gmail.com")

# password label and entry field and Generate button
password_label = Label(text="Password:", font=LABEL_FONT)
password_label.grid(column=0, row=3)

password_entry= ""

password_field = Entry()
password_field.grid(column=1, row=3, columnspan=1, sticky="ew")

generate_password_button = Button(text="Generate Password", font=LABEL_FONT, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="ew")

# Add button
add_button = Button(text="Add",
                    command=save_login)

add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=10)

# Keep window open
window.mainloop()
