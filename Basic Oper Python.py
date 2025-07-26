# Library Management System

booklist=[]

def addbook():
    name=input("Enter Book Name: ")
    price=int(input("Enter Book Price: "))
    year=int(input("Enter Book Year: "))
    booklist.append({"Name":name, "Price":price, "Year":year})

def searchbook(name):
    for x in booklist:
        if x["Name"]==name:
            return True
    return False

def deletebook():
    name=input("Enter Book Name to delete: ")
    if(searchbook(name)):
        for x in booklist:
            if x["Name"]==name:
                booklist.remove(x)
                print("Book Deleted Successfully")

def displaybook():
    for x in booklist:
        print(f"Name:" , x["Name"], "Price: ", x["Price"], "Year: ", x["Year"])

def updatebook():
    name=input("Enter Book Name to update: ")
    if(searchbook(name)):
        for x in booklist:
            if x["Name"]==name:
                print("1. To update Name")
                print("2. To update Price")
                print("3. To update Year")
                try:
                 choice = int(input("Enter your Choice"))
                 if choice == 1:
                   upname=input("Enter Name: ")
                   x["Name"]=upname
                 elif choice ==2:
                    uprice=int(input("Enter Price: "))
                    x["Price"]=uprice
                 elif choice==3:
                    upyear=int(input("Enter Year: "))
                    x["Year"]=upyear
                 else:
                     print("Invalid Choice")

                except ValueError:
                    print("Enter a Valid Number")
                return
    else: 
     print("Book not Found")

def main():
    print("Welcome to the Library Management System")
    while(1):
             
             print("1. Add Book")
             print("2. Delete Book")
             print("3. Display Books")
             print("4. Search Book")
             print("5. Update Book")
             print("6. Exit")
             try:
               choice=int(input("Enter your Choice: "))
               if choice==1:
                addbook()
               elif choice ==2:
                deletebook()
               elif choice==3:
                displaybook()
               elif choice == 4:
                name=input("Enter Book Name to Search: ")
                if(searchbook(name)):
                    print("Book Found")
                else :
                    print("Not Found")
               elif choice ==5:
                updatebook()
               elif choice == 6:
                 print("Exiting Library Management System")
                 break
               else:
                   print("Invalid Choice")
             except ValueError:
                 print("Invalid Input. Please enter a number between 1 and 6.")


if __name__== "__main__":
    main()
