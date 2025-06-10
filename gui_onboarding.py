import os
from tkinter import Tk, Label, Entry, Button, messagebox

def create_user(username):
    with open("user_registry.txt","a") as file:
        file.write(f"Created user: {username}\n")
def setup_folder(username):
    path= f"./home/{username}"
    os.makedirs(path, exist_ok=True)
def generate_email(username, email):
    content = f"""\
Subject: Welcome to the Team, {username}!

Hi {username},

Welcome aboard! Please review your onboarding checklist:
- Email: {email}
- VPN setup
- Slack & Zoom installed

Best,  
IT Support
"""
    with open(f"welcome_email_{username}.txt","w") as f:
        f.write(content)

def run_onboarding():
    username = entry_username.get()
    email = entry_email.get()
    if not username or not email:
        messagebox.showerror("Input Error", "Please enter both username and email")
        return
    create_user(username)
    setup_folder(username)
    generate_email(username, email)

    messagebox.showinfo("Success", f"Onboarding complete for {username}")
app = Tk()
app.title("IT Onboarding Toolkit")

Label(app, text="Username").grid(row=0, column=0, padx=10, pady=10)
entry_username = Entry(app, width=30)
entry_username.grid(row=0, column=1)

Label(app, text="Email:").grid(row=1, column=0, padx=10)
entry_email = Entry(app, width=30)
entry_email.grid(row=1, column=1)

Button(app, text="Run Onboarding", command=run_onboarding).grid(row=2, column=0, columnspan=2, pady=20)

app.mainloop()