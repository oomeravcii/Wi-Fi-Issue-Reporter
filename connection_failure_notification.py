import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

# Username and Password: "ÖmerAvcı","Admin123"

window = tk.Tk()

window.geometry("300x300")
window.config(bg="black")
window.title("Connection Failure Notification Sender")

# Title of the app.

text_title = tk.Label(window,text="Failure Notification Sender",bg="black",fg="white",font="Roboto 16 bold")
text_title.pack()

# Texts for username & password.

text_username = tk.Label(window,text="User Name:",bg="black",fg="white",font="Times 11 italic")
text_username.place(x=20,y=90)

text_password = tk.Label(window,text="Password:",bg="black",fg="white",font="Times 11 italic")
text_password.place(x=20,y=130)

# Entry boxes for username & password.

entry_username = tk.Entry(window)
entry_username.place(x=120,y=95)

entry_password = tk.Entry(window,show="*")
entry_password.place(x=120,y=135)

# Buttons for login and cancel.

def login():
    if entry_username.get() == "ÖmerAvcı" and entry_password.get() == "Admin123":
        msg = messagebox.showinfo(title="Well done!",message="Login successful.")
        if msg == "ok":
            window_form = tk.Toplevel()
            window_form.geometry("350x350")
            window_form.title("Failure Notification Form")
            window_form.config(bg="yellow")
            
            # Texts of the form.
            
            form_text_title = tk.Label(window_form,text="Failure Notification Form",bg="yellow",fg="black",font="Roboto 18 bold")
            form_text_title.pack()
            form_text_name_surname = tk.Label(window_form,text="Name-Surname:",font="consoles 12 italic",bg="yellow",fg="black")
            form_text_name_surname.place(x=40,y=50)
            form_text_id = tk.Label(window_form,text="Identification Number:",bg="yellow",fg="black",font="consoles 12 italic")
            form_text_id.place(x=40,y=90)
            form_text_modem = tk.Label(window_form,text="Modem Type:",font="consoles 12 italic",bg="yellow",fg="black")
            form_text_modem.place(x=40,y=130)
            form_text_failure = tk.Label(window_form,text="Failure Type:",font="consoles 12 italic",bg="yellow",fg="black")
            form_text_failure.place(x=40,y=170)
            form_text_adress = tk.Label(window_form,text="Adress:",font="consoles 12 italic",bg="yellow",fg="black")
            form_text_adress.place(x=40,y=210)
            form_text_mail = tk.Label(window_form,text="Mail:",font="consoles 12 italic",bg="yellow",fg="black")
            form_text_mail.place(x=40,y=250)
            
            # Entry & combo boxes of the form.
            
            form_entry_name = tk.Entry(window_form)
            form_entry_name.place(x=210,y=50)
            form_entry_id = tk.Entry(window_form)
            form_entry_id.place(x=210,y=90)
        
            # Random modem type names for the project. You can change them:
            modem_types = ["Tmp","KMP","FDP","4TkMn","NmTb","PnDs"]
            combo_modem = Combobox(window_form,values=modem_types)
            combo_modem.place(x=190,y=130)
            
            failure_types = ["Cable Issue","Login Failure","Not Able to connect Wi-Fi","Slow Network","Weak Wi-Fi Signal","Exhausted IP addresses"]
            combo_failure = Combobox(window_form,values=failure_types)
            combo_failure.place(x=190,y=170)
            
            form_entry_adress = tk.Entry(window_form)
            form_entry_adress.place(x=210,y=210)
            form_entry_mail = tk.Entry(window_form)
            form_entry_mail.place(x=210,y=250)
            
            # Button for failure form.
            
            def send():
                messagebox.showinfo(title="Done.",message="Fault notification message sent!")
            
            button = tk.Button(window_form,text="Send",command=send)
            button.place(x=210,y=290)
            
            
            
            
            window_form.mainloop()
            

def cancel():
    window.destroy()

button_login = tk.Button(window,text="Login",activebackground="green",bg="white",fg="black",command=login)
button_login.place(x=120,y=180,width=60)

button_cancel = tk.Button(window,text="Cancel",activebackground="red",bg="white",fg="black",command=cancel)
button_cancel.place(x=190,y=180,width=60)


window.mainloop()