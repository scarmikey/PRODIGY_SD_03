import tkinter as tk
from tkinter import messagebox
import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.contacts = []
        self.load_contacts()

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.edit_index = None

        self.build_gui()

    def build_gui(self):
        tk.Label(self.master, text="Name").grid(row=0)
        tk.Label(self.master, text="Phone").grid(row=1)
        tk.Label(self.master, text="Email").grid(row=2)

        tk.Entry(self.master, textvariable=self.name_var).grid(row=0, column=1)
        tk.Entry(self.master, textvariable=self.phone_var).grid(row=1, column=1)
        tk.Entry(self.master, textvariable=self.email_var).grid(row=2, column=1)

        self.contact_listbox = tk.Listbox(self.master)
        self.contact_listbox.grid(row=0, column=2, rowspan=4)

        tk.Button(self.master, text="Add", command=self.add_contact).grid(row=3, column=0)
        tk.Button(self.master, text="Edit", command=self.edit_contact).grid(row=3, column=1)
        tk.Button(self.master, text="Delete", command=self.delete_contact).grid(row=4, column=0)
        tk.Button(self.master, text="Save", command=self.save_contacts).grid(row=4, column=1)

        self.update_listbox()

    def add_contact(self):
        contact = Contact(self.name_var.get(), self.phone_var.get(), self.email_var.get())
        self.contacts.append(contact)
        self.update_listbox()

    def edit_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            self.edit_index = index
            contact = self.contacts[index]
            self.name_var.set(contact.name)
            self.phone_var.set(contact.phone)
            self.email_var.set(contact.email)
        except IndexError:
            messagebox.showinfo("Error", "No contact selected")

    def delete_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            self.contacts.pop(index)
            self.update_listbox()
        except IndexError:
            messagebox.showinfo("Error", "No contact selected")

    def save_contacts(self):
        with open('contacts.pkl', 'wb') as f:
            pickle.dump(self.contacts, f)

    def load_contacts(self):
        try:
            with open('contacts.pkl', 'rb') as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            pass

    def update_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact.name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
