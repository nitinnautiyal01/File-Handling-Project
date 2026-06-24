# CRUD Operations

from pathlib import Path
import os


# For creating file

def createfile():
    try:
        file_name = input("Create File name : ")
        path  = Path(file_name)

        if not path.exists():
            with open(path,"w") as file:
                    data = input("Write content : ") 
                    file.write(data)

            print("File Created Successfully!")

        else:
            print("File already exist!")

    except Exception as error:
        print(f"Error : {error}")
                

# For reading file

def readfile():
    try:
        name = input("File name : ")
        path = Path(name)
        
        if path.exists():
            with open(path,"r") as file:
                content = file.read()
                print(content)

        else:
            print("File not exist!")

    except Exception as error:
        print(f"Error : {error}")


# For updating file

def updatefile():

    try:
        name = input("File name : ")
        path = Path(name)

        if path.exists():
            print("What do you want to perform in update file")
            print("For renaming file, press 1")
            print("For appending the content, press 2")
            print("For overwriting the file, press 3")

            choice = int(input("Enter your choice : "))

            # For rename file name
            if choice == 1:
                newname = input("Tell Your new file name : ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("File rename successfully")

                else:
                    print("File name already exist!")
            
            #For adding content
            elif choice == 2:
                with open(path,"a") as file:
                    data = input("Enter Content : ")
                    file.write("\n" + data)
                    print("Successfully appended")
            
            #For Overwrite content
            elif choice == 3:
                with open(path,"w") as file:
                    data = input("Enter Content : ")
                    file.write(data)
                    print("Successfully Overwrite")

        else:
            print("File not exist!")

    except Exception as error:
        print(f"Error : {error}")


# For deleting file     
           
def deletefile():
    try:
        name = input("Enter your File name : ")
        path = Path(name)

        if path.exists():
            path.unlink()
            print("File Deleted")

        else:
            print("File not exist!")
    except Exception as error:
        print(f"Error : {error}")

# Choose Operations - CREATE, READ, UPDATE, DELETE

print("For Create file press 1")
print("For Read file press 2")
print("For Update file press 3")
print("For Delete file press 4")

choose = int(input("\nWhat do you want to perform : "))

if choose == 1:
    createfile()

if choose == 2:
    readfile()

if choose == 3:
    updatefile()

if choose == 4:
    deletefile()