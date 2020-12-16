import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9999))

while True:
    print("Python DB Menu")
    print("1. Find Customer")
    print("2. Add Customer")
    print("3. Delete Customer")
    print("4. Update Customer age")
    print("5. Update Customer address")
    print("6. Update Customer phone")
    print("7. Print report")
    print("8. Exit")
    option = input("Select : ")
    msg = b''
    if option == "1":
        name = input("Enter customer name to find : ")
        name = name.strip()
        while len(name) == 0:
            print("Enter valid name.")
            name = input("Enter customer name : ")
            name = name.strip()
        msg = bytes("1|"+name,'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        print(reply)
    if option == "2":
        name = input("Enter customer name : ")
        name = name.strip()
        while len(name) == 0:
            print("Enter valid name.")
            name = input("Enter customer name : ")
            name = name.strip()
        age = input("Enter age of customer : ")
        age = age.strip()
        if len(age) != 0:
            while not age.isnumeric():
                if len(age) == 0:
                    break
                print("Enter valid numeric age.")
                age = input("Enter age of customer : ")
                age = age.strip()
        address = input("Enter address of customer : ")
        address = address.strip()
        phone = input("Enter phone number : ")
        phone = phone.strip()
        msg = bytes("2|" + name + "|" + age + "|" + address + "|" + phone, 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        print(reply)
    if option == "3":
        name = input("Enter customer name to delete : ")
        name = name.strip()
        while len(name) == 0:
            print("Enter valid name.")
            name = input("Enter customer name : ")
            name = name.strip()
        msg = bytes("3|" + name, 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        print(reply)
    if option == "4":
        name = input("Enter customer name to update : ")
        name = name.strip()
        while len(name) == 0:
            print("Enter valid name.")
            name = input("Enter customer name : ")
            name = name.strip()
        age = input("Enter new age : ")
        age = age.strip()
        if len(age) != 0:
            while not age.isnumeric():
                if len(age) == 0:
                    break
                print("Enter valid numeric age.")
                age = input("Enter age of customer : ")
                age = age.strip()
        msg = bytes("4|" + name + "|" + age, 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        print(reply)
    if option == "5":
        name = input("Enter customer name to update : ")
        name = name.strip()
        while len(name) == 0:
            print("Enter valid name.")
            name = input("Enter customer name : ")
            name = name.strip()
        address = input("Enter new address : ")
        address = address.strip()
        msg = bytes("5|" + name + "|" + address, 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        print(reply)
    if option == "6":
        name = input("Enter customer name to update : ")
        name = name.strip()
        while len(name) == 0:
            print("Enter valid name.")
            name = input("Enter customer name : ")
            name = name.strip()
        phone = input("Enter new phone number : ")
        phone = phone.strip()
        msg = bytes("6|" + name + "|" + phone, 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        print(reply)
    if option == "7":
        msg = bytes("7|", 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        for key in sorted(reply.keys()):
            print(reply[key])
            print()
    if option == "8":
        print("Good Bye.")
        msg = bytes("8|", 'utf-8')
        s.send(msg)
        reply = s.recv(2048)
        reply = pickle.loads(reply)
        if reply == "Closed":
            s.close()
        exit()