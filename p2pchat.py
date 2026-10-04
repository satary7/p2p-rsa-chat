import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

my_ip = socket.gethostbyname(socket.gethostname())
port = int(input("Enter the port you want to operate on : "))
my_addr = (my_ip, port)
my_isinstance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_isinstance.bind(my_addr)

def send_msg(communication_socket):
    enxr = PKCS1_OAEP.new(RSA.import_key(recived_key))
    while True:
        msg = input("")
        communication_socket.send(enxr.encrypt(msg.encode("utf-8")))
        print(f"You>{msg}\n")
def recive_msg(communication_socket):
    dexnxr = PKCS1_OAEP.new(private_key)
    while True:
        rec_msg = communication_socket.recv(2048)
        print(f"Him>{dexnxr.decrypt(rec_msg).decode("utf-8")}\n")

print(f"Your address is {my_addr}")
while True:
    choice = input("would you like to start listening(1) for a connection or connect(2)? ")
    if choice.strip() == "1":
        print("Listening...")
        my_isinstance.listen(1)
        our_seesion, his_addr = my_isinstance.accept()
        print(f"{his_addr} is in")
        private_key = RSA.generate(2048)
        public_key = private_key.publickey()
        our_seesion.send(public_key.export_key())
        recived_key = our_seesion.recv(2048)
        t1 = threading.Thread(target=send_msg, args=(our_seesion,))
        t2 = threading.Thread(target=recive_msg, args=(our_seesion,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    elif choice.strip() == "2":
        his_port = input("Whats the other guys port ?")
        his_ip = input("whats his ip ?")
        my_isinstance.connect((his_ip, int(his_port)))
        print("You are in")
        private_key = RSA.generate(2048)
        public_key = private_key.publickey()
        my_isinstance.send(public_key.export_key())
        recived_key = my_isinstance.recv(2048)
        t1 = threading.Thread(target=send_msg, args=(my_isinstance,))
        t2 = threading.Thread(target=recive_msg, args=(my_isinstance,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        print("Enter a valid input")
