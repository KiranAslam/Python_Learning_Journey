def add_contact():
    try:
        with open("contacts.txt","a") as f:
            print("===================================================")
            name=input("Enter contact name:")
            phone=int(input("Enter phone number:"))
            email=input("Enter email address:")
            f.write(f"{name} | {phone} | {email} \n")
            print("===================================================")
            print("Contact added successfully!")
            print("===================================================")
    except ValueError:
        print("Invalid input. Please enter a valid phone number.")
    except Exception as e:
        print(f"error:{e}")

        
def view_contact():
    try:
        with open("contacts.txt", "r") as f:
            contacts=f.readlines()
            if not contacts:
                print("No contacts found.")
                return
            else:
                print("===================================================")
                for i, contact in enumerate(contacts, start=1):
                    parts=contact.strip().split('|')
                    print(f"Contact {i}:")
                    print(f"Name: {parts[0]} | Phone: {parts[1]} | Email: {parts[2]}")
                print("===================================================")
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as e:
        print(f"Error: {e}")

def search_contact():
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.readlines()
        if not contacts:
            print("No contacts found.")
            return
        search_name = input("Enter name to search: ").strip()
        found = False
        for contact in contacts:
            parts = contact.strip().split(' | ')
            if len(parts) == 3:
                if search_name.lower() == parts[0].strip().lower():
                    print("\nContact Found:")
                    print(f"Name: {parts[0]} | Phone: {parts[1]} | Email: {parts[2]}")
                    found = True
                    break
        
        if not found:
            print("Contact not found.")
            
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as e:
        print(f"Error: {e}")

def delete_contact():
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.readlines()
        if not contacts:
            print("No contacts found.")
            return
        view_contact()
        delete_c = int(input("Enter the contact number to delete: "))
        if 1 <= delete_c <= len(contacts):
            contacts.pop(delete_c - 1)
            with open("contacts.txt", "w") as f:
                f.writelines(contacts)   
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")       
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")

def update_contact():
    try:
        with open("contacts.txt", "r") as f:
            contacts=f.readlines()
            if not contacts:
                print("no contacts found.")
                return
            else:
                    view_contact()
                    update_contact=int(input("Enter the contact number to update: "))
                    if 1<=update_contact<=len(contacts):
                        print("Enter new details for the contact:")
                        new_name=input("Enter new name: ")
                        new_phone=int(input("Enter new phone number: "))
                        new_email=input("Enter new email:")
                        contacts[update_contact-1]=f"{new_name}|{new_phone}|{new_email}\n"
                        
                        with open("contacts.txt", "w") as f:
                            for contact in contacts:  
                                f.write(contact)
                        print("Contact updated successfully!")
                    else:
                        print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")
    except FileNotFoundError:
        print("No contacts found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        while True:
            print("===================================================")
            print("          Contact Book Management System          ")
            print("===================================================")
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. Delete Contact")
            print("4. Update Contact")
            print("5. View Contact")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                search_contact()
            elif choice == 3:
                delete_contact()
            elif choice == 4:
                update_contact()
            elif choice == 5:
                view_contact()
            elif choice == 6:
                print("==============================================")
                print("Exiting Contact Book Management System.")
                print("==============================================")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
main()