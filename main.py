from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    new_data = {website:
                    {"email": email,
                     "password":password,
                     }
                }
    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title="Oops" , message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json" , "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json" , "w") as data_file:
                json.dump(new_data , data_file , indent = 4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json" , "w") as data_file:
                #Saving updated data
                json.dump(data , data_file , indent = 4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json" , "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error!" , message = "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}" , message = f"Email:{email} \n Password:{password}")
        else:
            messagebox.showinfo(title = "Error!" , message = f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50 , pady = 50)

canvas = Canvas(width = 200 , height = 200 , highlightthickness=0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column = 1 , row = 0)

#Labels
website_label = Label(text = "Website:")
website_label.grid(column = 0 , row = 1)

mail_label = Label(text = "Email/Username:")
mail_label.grid(column = 0 , row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0 , row = 3)

#Enteries
website_entry = Entry(width = 35)
website_entry.grid(column = 1 , row = 1)
website_entry.focus()

mail_entry = Entry(width = 54)
mail_entry.grid(column = 1 , row = 2, columnspan = 2)
mail_entry.insert(0 , "abhinand@gmail.com")

password_entry = Entry(width = 35)
password_entry.grid(column = 1 , row = 3)

#Buttons
generate_pass = Button(text = "Generate Password" , command = generate_password)
generate_pass.grid(column = 2 , row = 3)

add_button = Button(text = "Add" , width = 30 , command = save_info)
add_button.grid(column = 1 , row = 4)

search_button = Button(text = "Search",width  = 14 , command = find_password)
search_button.grid(column = 2 , row = 1)

window.mainloop()



















