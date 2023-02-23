from ast import Delete
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
#Password Generator Project
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters=[choice(letters) for _ in range(randint(8,10))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]
    password_list= password_letters+ password_symbols+ password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
window=Tk()
window.config(padx=50,pady=20)
window.title("Password Manager")
canvas=Canvas(height=200,width=200)
lock_image=PhotoImage(file="lock.png")
canvas.create_image(100,100,image= lock_image)
canvas.grid(row=0,column=1)
#columnspan grid fonksiyonunun yarattýðý ýzgaralarýn yayýlma miktarýný ayarlar.
#Label
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_username=Label(text="E-mail/Username: ")
email_username.grid(row=2,column=0)
password_label=Label(text="Password: ")
password_label.grid(row=3,column=0)
#Entry
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1,sticky="EW")
website_entry.focus() #program açýldýðýnda o giriþe otomatik yazým olarak baþlar
email_username_entry=Entry(width=35)
email_username_entry.grid(row=2,column=1,sticky="EW")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,sticky="EW")
#save fonksiyonu ile dosyayý kaydetme
def save():
    email_text=email_username_entry.get()
    website_text= website_entry.get()
    password_text= password_entry.get()
    new_data={
        website_text:{
            "email": email_text,
            "password": password_text,
            }
        }
    if len( email_text)==0 or len( website_text)==0 or len( password_text )==0:
        messagebox.showinfo(title="ERROR",message="Please make sure you haven't left any fields empty.")
    else:  
        try:
            with open("information.json","r") as info:
                data=json.load(info)
        except (FileNotFoundError, json.decoder.JSONDecodeError ):
            with open("information.json","w") as info:
                json.dump(new_data,info, indent=4)
        else:
            data.update(new_data)
            with open("information.json","w") as info: 
                json.dump(data, info, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)  
#search fonksiyonunu oluþturma:
def find_password():
    website= website_entry.get()
    try:
        with open("information.json","r") as info:
            data=json.load(info)
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="ERROR",message= "File Not Found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website, message=(f"E-mail:{email}\nPassword: {password}"))
        else:
            messagebox.showinfo(title="Error", message=(f"No details for {website} exist."))

#Button
password_button=Button(text="Generate Password",command=password_generate)
password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")
search_button=Button(text="Search",command=find_password,width=14)
search_button.grid(row=1,column=2,columnspan=2)



window.mainloop()








