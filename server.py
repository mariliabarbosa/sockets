import socket

name = "Caio"
cpf = "023.829.345-82"
rg = "92355678"
birthday = "02-04-1998"
register_number = "293456"

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Conexão Estabelecida - {address[0]}:{address[1]}")

        string = client.recv(1024)
        string = string.decode("utf-8")

        if (string == "nome"):
            client.send(bytes(name, "utf-8"))
        elif (string == "cpf"):
            client.send(bytes(cpf, "utf-8"))
        elif (string == "rg"):
            client.send(bytes(rg, "utf-8"))
        elif (string == "data de nascimento"):
            client.send(bytes(birthday, "utf-8"))
        elif (string == "matricula"):
            client.send(bytes(register_number, "utf-8"))

        client.close()
