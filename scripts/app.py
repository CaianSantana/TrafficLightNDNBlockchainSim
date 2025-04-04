import threading
import time
import socket
import random
from fluxo import Fluxo
from semaforo import Semaforo
from multidao import Multidao
from transito import Transito

# Instância do semáforo
semaforo = Semaforo()
multidao = Multidao()
transito = Transito(10, 2, 60, 8, Fluxo.MEDIO)


def muda_temṕo():
    while True:
        transito.chegar_carro()
        multidao.chegar_pedestre()
        if semaforo.corAtual == "VERMELHO":
            transito.frear()
            multidao.atravessar()
        elif semaforo.corAtual == "AMARELO":
            transito.reduzir()
        else:
            transito.avancar()
        time.sleep(1)



thread_tempo = threading.Thread(target=semaforo.contar_tempo)
thread_muda_tempo = threading.Thread(target=muda_temṕo)


thread_tempo.start()
thread_muda_tempo.start()
