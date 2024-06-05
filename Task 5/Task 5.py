import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
        messagebox.showinfo("Success", "Contact added successfully!")

    def delete_contact(self, index):
        del self.contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def update_contact(self, index, name, phone, email, address):
        self.contacts[index] = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact updated successfully!")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                results.append(contact)
        return results

    def get_contacts(self):
        return self.contacts

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")

        self.contact_book = ContactBook()

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.name_label = tk.Label(root, text="Name:", padx=10, pady=5)
        self.name_label.grid(row=0, column=0, sticky='w')

        self.name_entry = tk.Entry(root, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:", padx=10, pady=5)
        self.phone_label.grid(row=1, column=0, sticky='w')

        self.phone_entry = tk.Entry(root, textvariable=self.phone_var)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:", padx=10, pady=5)
        self.email_label.grid(row=2, column=0, sticky='w')

        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address:", padx=10, pady=5)
        self.address_label.grid(row=3, column=0, sticky='w')

        self.address_entry = tk.Entry(root, textvariable=self.address_var)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg='sky blue', fg='white', padx=10, pady=5)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, bg='light green', fg='black', padx=10, pady=5)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.search_label = tk.Label(root, text="Search:", padx=10, pady=5)
        self.search_label.grid(row=6, column=0, sticky='w')

        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contacts, bg='light coral', fg='black', padx=10, pady=5)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.contact_listbox = tk.Listbox(root, bg='light grey', fg='black', width=40, height=10)
        self.contact_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.contact_listbox.bind('<<ListboxSelect>>', self.on_contact_select)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, bg='light coral', fg='black', padx=10, pady=5)
        self.delete_button.grid(row=9, column=0, padx=10, pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, bg='light green', fg='black', padx=10, pady=5)
        self.update_button.grid(row=9, column=1, padx=10, pady=5)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone:
            self.contact_book.add_contact(name, phone, email, address)
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contact_book.get_contacts():
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def search_contacts(self):
        search_term = self.search_entry.get()
        self.contact_listbox.delete(0, tk.END)
        results = self.contact_book.search_contact(search_term)
        for contact in results:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def on_contact_select(self, event):
        try:
            index = self.contact_listbox.curselection()[0]
            contact = self.contact_book.get_contacts()[index]
            self.name_var.set(contact['Name'])
            self.phone_var.set(contact['Phone'])
            self.email_var.set(contact['Email'])
            self.address_var.set(contact['Address'])
        except IndexError:
            pass

    def delete_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            self.contact_book.delete_contact(index)
            self.clear_entries()
            self.view_contacts()
        except IndexError:
            messagebox.showerror("Error", "No contact selected.")

    def update_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            name = self.name_var.get()
            phone = self.phone_var.get()
            email = self.email_var.get()
            address = self.address_var.get()
            self.contact_book.update_contact(index, name, phone, email, address)
            self.clear_entries()
            self.view_contacts()
        except IndexError:
            messagebox.showerror("Error", "No contact selected.")

    def clear_entries(self):
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.address_var.set('')

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
