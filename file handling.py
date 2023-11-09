print("_______________________________")
print("*         FILE HANDLING                *")
print("_______________________________")
import os
while True:
        def  f():
            print("1.create the file")
            print("2.read the file")
            print("3.list the file")
            print("4.edit the file")
            print("5.delete the file")
            print("6.stop program")
        a=input("enter the choice:")
        match a:
            case "1":
                print("creating a file")
                name=input("enter file name:")
                name=name+".txt"
                file=open(name,"w")
                file.write("welcome")
                print("----------------------------------")
                print("file created successfully")
                print("----------------------------------")
                f()
            case "2":
                print("read the file")
                name=input("enter file name:")
                name=name+".txt"
                file=open(name,"r")
                print("---------------------------------------")
                print(file.read())
                print("---------------------------------------")
                f()
            case "3":
                print("listing the file")
                print("____________________")
                path="D:\meghana"
                file=os.listdir(path)
                for file in file:
                    print(file)
                print("____________________")
                f()
            case "4":
                print("editing the file")
                name=input("enter file name:")
                name=name+".txt"
                file=open(name,"a")
                print(file.write("meghana"))
                print("__________________")
                print("edited the file")
                print("__________________")
            case "5":
                print("deleting the file")
                name=input("enter file name:")
                name=name+".txt"
                os.remove(name)
                print("file",name,"deleted successfully")
                print("__________________")
            case "6":
                print("stop the program")
print("end")
        
    
        
