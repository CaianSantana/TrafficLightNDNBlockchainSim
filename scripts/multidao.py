import random
import time

class Multidao():
    def __init__(self):
        self.quantidade_pessoas= 0

    def chegar_pedestre(self):
        pedestres = random.randint(0, 5)
        self.quantidade_pessoas+= pedestres
        print(f"{pedestres} novos pedestres chegaram! Total: {self.quantidade_pessoas}")

    def atravessar(self):
        self.chegar_pedestre()
        print(f"{self.quantidade_pessoas} pedestres atravessaram!")
        self.quantidade_pessoas= 0
        