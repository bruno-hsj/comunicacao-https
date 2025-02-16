"""
Módulo de Testes para Comunicação HTTPS

Este script inicia um servidor HTTPS em segundo plano e executa testes de comunicação
entre um cliente e o servidor. Ele verifica se o cliente consegue se conectar corretamente
e se o servidor responde de forma esperada.

Módulos Importados:
- subprocess: Para executar o servidor em um processo separado.
- time: Para adicionar um pequeno atraso antes de conectar o cliente.
- sys: Para obter o interpretador Python em execução.
- cliente.client: Importa a função `run_client()` para iniciar o cliente.
- servidor.server: Importa a função `run_server()` para iniciar o servidor.
"""

import subprocess
import time
import sys
from cliente.client import run_client  # Importa a função do cliente
from servidor.server import run_server  # Importa a função do servidor

def start_server():
    print("--- Iniciando servidor HTTPS ---")
    server_process = subprocess.Popen([sys.executable, "servidor/server.py"])
    time.sleep(2)
    return server_process

def run_tests():
    print("Executando teste cliente-servidor \n")

    server_process = start_server()

    try:
        print("\nConectando cliente ao servidor\n")
        response = run_client()
        print("\nResposta do servidor:\n", response)

        if response != None:
            print("\nTeste de comunicação: OK\n")
        else:
            print("\nTeste de comunicação: Falhou\n")

    finally:
        print("Encerrando servidor.")
        server_process.terminate()

if __name__ == "__main__":
    run_tests()