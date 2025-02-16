"""
Servidor HTTPS Simples

Este módulo implementa um servidor HTTPS básico usando sockets e SSL/TLS.
O servidor escuta conexões na porta 8443 e responde com uma mensagem simples.

Módulos Importados:
- socket: Para criar e gerenciar conexões de rede.
- ssl: Para adicionar suporte a conexões seguras via TLS/SSL.
"""

import socket, ssl

def run_server():
    HOST = '0.0.0.0' 
    PORT = 8443

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    context.load_cert_chain(certfile=".\servidor\cert.pem", keyfile=".\servidor\key.pem")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)

        print(f"--- Servidor HTTPS funcionando! Escutando em: {HOST}:{PORT} ---")

        with context.wrap_socket(sock, server_side=True) as Ssock:
            while True:
                connection, address = Ssock.accept()
                print(f"--- Conexão estabelecida com o endereco: {address} ---")
                connection.send(b"\nHTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n--- Mensagem resposta do servidor: Oi, mundo! ---")

                connection.close()

if __name__ == "__main__":
    run_server()