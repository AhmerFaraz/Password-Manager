from tkinter import *
from tkinter import messagebox
import random
import json

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_random = ""
    for char in password_list:
        password_random += char

    pass_entry.delete(0, END)
    pass_entry.insert(END, password_random)


def save():
    company = company_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        company: {
            "email": email,
            "password": password,
        }
    }

    if len(company) == 0 and len(password) == 0:
        messagebox.askretrycancel(title="Invalid company name & password", message="Invalid company name and password\nThese fields cannot remain empty\nPress retry.")

    elif len(company) == 0:
        messagebox.askretrycancel(title="Invalid company name", message="Invalid company name\nCompany name should not be empty or invalid\nPress retry.")
    
    elif len(password) == 0:
        messagebox.askretrycancel(title="Invalid Password", message="Invalid Password\n Password should not be empty or incorrect/npress retry.")

    else:
        is_ok = messagebox.askokcancel(title="Confirm details", message=f"These are the details:\ncompany: {company}\nEmail: {email}\nPassword: {password}\n Is it ok to save.")

        if is_ok:
            try:
                with open("Day-29/data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                    with open("Day-29/data.json", "w") as data_file:
                         json.dump(new_data, data_file, indent= 4)

            else:
                data.update(new_data)

                with open("Day-29/data.json", "w") as data_file:
                    json.dump(data, data_file, indent= 4)

            finally:
                company_entry.delete(0, END)
                pass_entry.delete(0, END)
                company_entry.focus()
                email_entry.delete(0, END)
                email_entry.insert(0, "example@gmail.com")  

def find_password():
    company = company_entry.get()
    try:
        with open("Day-29/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "No Data File Found")
    else:
        if company in data:
            email = data[company]["email"]
            password = data[company]["password"]
            messagebox.showinfo(title= company, message= f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message= f"No details for {company} exists.")

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
logo_image = PhotoImage(file="Day-29/logo.png")
canvas.create_image(100, 100, image=logo_image)

company = Label(text="company: ")
company.grid(row=1, column=0)

company_entry = Entry(width=21)
company_entry.grid(row=1, column=1)
company_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", command=pass_gen)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text= "Search", width=13, command= find_password)
search_button.grid(row= 1, column= 2)

window.mainloop()
