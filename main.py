import json

contacts = []

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []


def add_contact(name, phone):
    contacts.append({'name': name, 'phone': phone})

def list_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for c in contacts:
        print(f"Name: {c['name']}, Phone: {c['phone']}")

def search_contact(name):
    found = False
    for c in contacts:
        if c["name"] == name:
            print(f"Name: {c['name']}, Phone: {c['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact(name):
    found = False
    for index, c in enumerate(contacts):
        if c["name"] == name:
            contacts.pop(index)
            found = True
    if found:
        print(f"Contact {name} deleted.")
    if not found:
            print("Contact not found.")

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
    
            

while True:
   
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
        save_contacts()
    elif choice == "2":
        list_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)
        save_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
    
    