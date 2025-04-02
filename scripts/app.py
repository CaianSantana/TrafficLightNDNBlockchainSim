import threading
import time
import socket
import random
from semaforo import Semaforo
from multidao import Multidao
from transito import Transito

# Instância do semáforo
semaforo = Semaforo()
multidao = Multidao()
transito = Transito()


def muda_temṕo():
    while True:
        if semaforo.corAtual == "VERMELHO":
            transito.frear()
            multidao.atravessar()
            time.sleep(semaforo.tempo)
        elif semaforo.corAtual == "AMARELO":
            transito.reduzir()
            multidao.chegar_pedestre()
        else:
            transito.avancar()
            semaforo.alterar_tempo(0)
            multidao.chegar_pedestre()
        time.sleep(random.randint(0, max(1,semaforo.tempo_cores.get(semaforo.corAtual))))



thread_tempo = threading.Thread(target=semaforo.contar_tempo)
thread_muda_tempo = threading.Thread(target=muda_temṕo)


thread_tempo.start()
thread_muda_tempo.start()
