import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDRESS = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

FOLDERS = ["Documents", "Music", "Video", "Image", "Desktop"]

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)

        if msg == DISCONNECT_MSG:
            connected = False
        
        print(f"[{addr}] {msg}")
        response = f"Mensagem recebida: {msg}"
        
        if msg == "ls":
            folders = ""
            for folder in FOLDERS:
                folders += f" {folder}"
            print(msg)
            conn.send(f"{response}\nResposta: {folders}".encode(FORMAT))
        else:
            conn.send(f"{response}".encode(FORMAT))
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    print(f"[ESCUTANDO] O servidor está escutando a porta {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.active_count() - 1}")
if __name__ == "__main__":
    main()