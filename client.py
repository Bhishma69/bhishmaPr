import threading
import socket

host = '127.0.0.1'  # local host
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"conneted with : {str(address)} ")

        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'ye bhadwe kaa naam  {nickname} :)')
        broadcast(f'{nickname} aagaya  '.encode('ascii'))
        client.send('gand mara ab idhar  '.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("server sun raha hai ..")
receive()
