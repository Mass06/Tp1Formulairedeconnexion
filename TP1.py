from tkinter import *
from PIL import Image, ImageTk
import csv
import os
import hashlib

root = Tk()
root.title("TP1 : Sécurité des systèmes d'informations ")
root.geometry("1000x750")



def show_password():
    # Fonction pour afficher ou masquer le mot de passe
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
def show_password2():
   
    if show_newpassword_var.get():
        newpassword_entry.config(show="")
    else:
        newpassword_entry.config(show="*")
def show_password3():
   
    if show_newpassword2_var.get():
        newconfirmpassword_entry.config(show="")
    else:
        newconfirmpassword_entry.config(show="*")

show_password_var = BooleanVar()
show_password_var.set(False)

show_password_button = Checkbutton(root, text="Afficher le mot de passe", variable=show_password_var, command=show_password)
show_password_button.grid(row=2, column=3, pady=10)

show_newpassword_var = BooleanVar()
show_newpassword_var.set(False)

show_newpassword2_var = BooleanVar()
show_newpassword2_var.set(False)


def show_welcome_page():
    # Fonction pour afficher la nouvelle page de bienvenue
    welcome_window = Toplevel(root)
    welcome_window.title("Bienvenue ")
    welcome_window.geometry("500x350")
    welcome_label = Label(welcome_window, text="Bienvenue ! ")
    welcome_label.pack(pady=20)

    logout_button = Button(welcome_window, text="Déconnexion", command=welcome_window.destroy, bg="red")
    
    logout_button.pack()
# Création du fichier CSV s'il n'existe pas
csv_filename = "users.csv"
if not os.path.exists(csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])

def reset_fields():
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def newreset_fields():
    newusername_entry.delete(0, END)
    newpassword_entry.delete(0, END)
    newconfirmpassword_entry.delete(0, END)

def hash_password(password):
    # Fonction pour hacher le mot de passe avec SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_credentials():
    entered_username = username_entry.get()
    entered_password = hash_password(password_entry.get())
    if not entered_username or not entered_password:
        result_label.config(text="Erreur : Veuillez remplir tous les champs!", fg="red")
        return
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == entered_username and row["password"] == entered_password:
                result_label.config(text="Connexion réussie", fg ="green")
                show_welcome_page()
                return
           

    result_label.config(text="Connexion échouée", fg="red")
    reset_fields() 

def add_account():
    global newusername_label, newpassword_label, newconfirmpassword_label, newusername_entry, newpassword_entry, newconfirmpassword_entry, save_btn

    if 'new_username_label' in globals():
        newusername_label.destroy()
        newpassword_label.destroy()
        newconfirmpassword_label.destroy()
        newusername_entry.destroy()
        newpassword_entry.destroy()
        newconfirmpassword_entry.destroy()
        save_btn.destroy()
    
    Label(root, text="Inscription ", font="arial 15 bold").grid(row=7, column=1, columnspan=3, pady=10)
    show_newpassword_button = Checkbutton(root, text="Afficher le mot de passe", variable=show_newpassword_var, command=show_password2)
    show_newpassword_button.grid(row=9, column=3, pady=10)

    show_newpassword2_button = Checkbutton(root, text="Afficher le mot de passe", variable=show_newpassword2_var, command=show_password3)
    show_newpassword2_button.grid(row=10, column=3, pady=10)

    newusername_label = Label(root, text="Identifiant")
    newpassword_label = Label(root, text="Mot de passe")
    newconfirmpassword_label = Label(root, text="Confirmer le mot de passe")

    newusername_label.grid(row=8, column=1)
    newpassword_label.grid(row=9, column=1)
    newconfirmpassword_label.grid(row=10, column=1)

    newusername_value = StringVar()
    newpassword_value = StringVar()
    newconfirmpassword_value = StringVar()
    
    newreset_btn = Button(text="Réinitialiser", command=newreset_fields)
    newreset_btn.grid(row=11, column=1)

    newusername_entry = Entry(root, textvariable=newusername_value)
    newpassword_entry = Entry(root, textvariable=newpassword_value, show="*")  
    newconfirmpassword_entry = Entry(root, textvariable=newconfirmpassword_value, show="*")  

    newusername_entry.grid(row=8, column=2)
    newpassword_entry.grid(row=9, column=2)
    newconfirmpassword_entry.grid(row=10, column=2)
    
    save_btn = Button(text="Enregistrer", command=save_new_account, bg="green")
    save_btn.grid(row=11, column=2, pady=10)

 

def save_new_account():
    new_username = newusername_entry.get()
    new_password = newpassword_entry.get()
    confirm_password = newconfirmpassword_entry.get()

    # Vérification si les champs ne sont pas vides
    if not new_username or not new_password:
        newresult_label.config(text="Erreur : Veuillez remplir tous les champs!", fg="red")
        return

    # Vérification si le mot de passe est différent de l'identifiant
    if new_username == new_password:
        newresult_label.config(text="Erreur : Le mot de passe doit être différent de l'identifiant!", fg="red")
        return
      # Vérification de la longueur du mot de passe
    if len(new_password) < 8:
        newresult_label.config(text="Erreur : Le mot de passe doit contenir au moins 8 caractères!", fg="red")
        return
    # Vérification si les mots de passe saisis correspondent
    if new_password != confirm_password:
        newresult_label.config(text="Erreur : Les mots de passe saisis ne correspondent pas.", fg="red")
        return

    # Vérification de la robustesse du mot de passe
    if not any(char.isupper() for char in new_password) or \
       not any(char.islower() for char in new_password) or \
       not any(char.isdigit() for char in new_password) or \
       not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in new_password):
        newresult_label.config(text="Erreur : Le mot de passe doit contenir au moins une majuscule, une minuscule, un chiffre et un symbole!", fg="red")
        return

    # Hachage du mot de passe
    hashed_password = hash_password(new_password)

    
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_username, hashed_password])

    newresult_label.config(text="Compte ajouté avec succès", fg="green")
    newreset_fields()


# Ajout d'un logo
logo_image = Image.open("logo.png") 
logo_image = logo_image.resize((160, 50), Image.BICUBIC)
logo = ImageTk.PhotoImage(logo_image)
logo_label = Label(root, image=logo)
logo_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

Label(root, text="Formulaire de connexion ", font="arial 15 bold").grid(row=0, column=1, columnspan=3, pady=10)
username_label = Label(root, text="Identifiant")
password_label = Label(root, text="Mot de passe")



username_label.grid(row=1, column=1)
password_label.grid(row=2, column=1)



username_value = StringVar()
password_value = StringVar()


newresult_label = Label(root, text="")
newresult_label.grid(row=12, column=2, pady=10)
username_entry = Entry(root, textvariable=username_value)
password_entry = Entry(root, textvariable=password_value, show="*")  



username_entry.grid(row=1, column=2)
password_entry.grid(row=2, column=2)



result_label = Label(root, text="")
result_label.grid(row=4, column=2, pady=10)



reset_btn = Button(text="Réinitialiser", command=reset_fields)
newreset_btn = Button(text="Réinitialiser", command=reset_fields)
ok_btn = Button(text="Se connecter", command=check_credentials, bg="green")
add_account_btn = Button(text="Ajout compte", command=add_account)

reset_btn.grid(row=3, column=1)
ok_btn.grid(row=3, column=2)
add_account_btn.grid(row=3, column=3)

root.mainloop()