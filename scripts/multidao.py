import random
from fluxo import Fluxo

class Multidao():
    def __init__(self, fluxo=Fluxo.BAIXO):
        self.quantidade_pessoas= 0
        self.fluxo = fluxo

    def chegar_pedestre(self):
        pedestres=0
        if random.randint(1,4) <= self.fluxo.value:
            pedestres = random.randint(1, 5)
            self.quantidade_pessoas+= pedestres

    def atravessar(self):
        self.chegar_pedestre()
        print(f"\n{self.quantidade_pessoas} pedestres atravessaram!")
        self.quantidade_pessoas= 0
        