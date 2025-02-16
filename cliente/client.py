"""
Cliente HTTPS Simples

Este módulo implementa um cliente HTTPS básico que se conecta a um servidor 
seguro usando sockets e SSL/TLS.

Módulos Importados:
- socket: Para criar e gerenciar conexões de rede.
- ssl: Para adicionar suporte a conexões seguras via TLS/SSL.
"""

import socket, ssl

def run_client():
    HOST = 'localhost'
    PORT = 8443

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE


    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname = HOST) as Ssock:
            print("--- Conexão com o servidor HTTPS realizada! ---")
            response = Ssock.recv(1024)

            return response.decode()

if __name__ == "__main__":
    print(run_client)