def add_book():
    try:
        book_title= input("Enter the title of the book: ")
        author=input("Enter the author of the book: ")
        with open("library.txt","a") as f:
            f.write(book_title + ":" + author + "\n")
            print("Book added successfully!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print("An error occurred:", e)

def view_book():
    try:
        with open("library.txt","r") as f:
            content=f.read()
            if content:
                for i in content.splitlines():
                    print("====Available Books====\n")
                    print(i)
            else:
                print("The file is empty!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print("An error occurred:", e)

def search_book():
    try:
        s_book=input("Enter the book name you want to search: ").strip().lower()
        found=False
        with open("library.txt","r") as f:
            for line in f:
                if s_book in line.lower():
                    print(f"Book found! {line.strip()}")
                    found=True
            if not found:
                print("Book not found!")
            
    except ValueError:
        print("invalid input!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print("An error occurred:", e)               
def delete_book():
    try:
        d_book=input("Enter the book name you want to delete: ").strip().lower()
        with open("library.txt","r") as f:
            lines=f.readlines()
            found=False
            new_lines=[]
            for line in lines:
                if d_book not in line.lower():
                    new_lines.append(line)
                else:
                    found=True
            if found:
                with open("library.txt", "w") as f:
                    f.writelines(new_lines)
                print("Book deleted successfully!")
            else:
                print("File is empty!")
            
    except ValueError:
        print("invalid input!")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print("An error occurred:", e)


def main():
    while True:
        try:
            print("===============Welcome to Library mangement system=============")
            print("1. add book. ")
            print("2. view book. ")
            print("3. search a book.")
            print("4. delete a book. ")
            print("5. Exit")

            choice=int(input("Enter your choice(1-5):  "))
            if choice==5:
                print("Thank you for using our system!")
                break
            elif choice==1:
                add_book()
            elif choice==2:
                view_book()
            elif choice==3:
                search_book()
            elif choice==4:
                delete_book()
            else:
                print("")
        except ValueError:
            print("Invalid Input! Please try again later!")

main()