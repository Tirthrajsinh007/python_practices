contacts = {}

def insert():
    name = input("Enter Name :")
    num = input("Enter Contact Number :")
    contacts[name] =num

def display():
    print("======= the contact details ============")
    for name,num in contacts.items():
        print(name,num,sep=" -> ")
    print("========================================")

def edit():
    print("======= Welcome to Edit Menu ===========")
    search =input("Enter name where you want to update :")
    for name in contacts:
        
        if search == name:
            edit_num = input("Enter Number To Update :")
            contacts[search] = edit_num
            print("Contact Update Successfully.....")
        else:
            print("Enter Valid name...")
            break;

        
while True:
    print("\n1.Insert \n2.display \n3.edit \npress other keys to exit")
    ch =int(input("Enter Choice :"))
    if(ch == 1):
        insert();
    elif ch == 2:
        display();
    elif ch ==3:
        edit();
    else:
        print("Exiting....");
        break;
