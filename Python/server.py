import socket
import pickle

try:
    with open("data.txt") as fobj:
        text = fobj.read()
except FileNotFoundError:
    text = None
data = {}
new_text = text.split("\n")

for tobj in range(len(new_text)):
    user = new_text[tobj]
    info = user.split("|")
    name = info[0].rstrip().lstrip().lower()
    if name == "":
        continue
    age = info[1].rstrip().lstrip()
    if not age.isnumeric():
        age = ""
    address = info[2].rstrip().lstrip()
    phone = info[3].rstrip().lstrip()
    lis = [name, age, address, phone]
    data[name] = lis

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    try:
        while True:
            msg = clientsocket.recv(2048)
            if len(msg) != 0:
                msg = msg.decode("utf-8")
                code = msg.split("|")
                code[0] = int(code[0])
                reply = b''
                code[1] = code[1].lower()
                if code[0] == 1:
                    if code[1] in data:
                        reply = pickle.dumps(data[code[1]])
                    else:
                        reply = pickle.dumps("No data found for "+code[1])
                    clientsocket.send(reply)
                elif code[0] == 2:
                    if code[1] in data:
                        reply = pickle.dumps("Customer already exists.")
                    else:
                        lis = [code[1], code[2], code[3], code[4]]
                        data[code[1]] = lis
                        reply = pickle.dumps("Customer added.")
                    clientsocket.send(reply)
                elif code[0] == 3:
                    if code[1] in data:
                        del data[code[1]]
                        reply = pickle.dumps("Customer data deleted.")
                    else:
                        reply = pickle.dumps("No data found for " + code[1])
                    clientsocket.send(reply)
                elif code[0] == 4:
                    if code[1] in data:
                        data[code[1]][1] = code[2]
                        reply = pickle.dumps("Customer age updated.")
                    else:
                        reply = pickle.dumps("No data found for " + code[1])
                    clientsocket.send(reply)
                elif code[0] == 5:
                    if code[1] in data:
                        data[code[1]][2] = code[2]
                        reply = pickle.dumps("Customer address updated.")
                    else:
                        reply = pickle.dumps("No data found for " + code[1])
                    clientsocket.send(reply)
                elif code[0] == 6:
                    if code[1] in data:
                        data[code[1]][3] = code[2]
                        reply = pickle.dumps("Customer phone number updated.")
                    else:
                        reply = pickle.dumps("No data found for " + code[1])
                    clientsocket.send(reply)
                elif code[0] == 7:
                    reply = pickle.dumps(data)
                    clientsocket.send(reply)
                elif code[0] == 8:
                    reply = pickle.dumps("Closed")
                    clientsocket.send(reply)
                    break
    except:
        continue