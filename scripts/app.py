import threading
import time
import socket
import random
from semaforo import Semaforo

# Instância do semáforo
semaforo = Semaforo()

def muda_temṕo():
    while True:
        print("mudando tempo")
        semaforo.alterar_tempo(-5)
        time.sleep(16)


thread_tempo = threading.Thread(target=semaforo.contar_tempo)
thread_muda_tempo = threading.Thread(target=muda_temṕo)


thread_tempo.start()
thread_muda_tempo.start()
