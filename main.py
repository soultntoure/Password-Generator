from tkinter import * 
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols =  [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
         website: {
              "username": username,
              "password": password,
         }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you fill all the fields")
    else:    
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:    
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            
            with open("data.json", "w") as data_file:    
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)   


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50)



canvas = Canvas(width = 200 , height = 200, highlightthickness= 0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(END, "soult@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()