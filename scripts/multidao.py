import random
from fluxo import Fluxo

class Multidao:
    def __init__(self, fluxo=Fluxo.BAIXO):
        self._quantidade_pessoas = 0
        self._fluxo = fluxo

    # Getter somente leitura
    @property
    def quantidade_pessoas(self):
        return self._quantidade_pessoas

    # Getter e setter de fluxo
    @property
    def fluxo(self):
        return self._fluxo

    @fluxo.setter
    def fluxo(self, novo_fluxo):
        if isinstance(novo_fluxo, Fluxo):
            self._fluxo = novo_fluxo
        else:
            raise ValueError("⚠️ O fluxo deve ser uma instância válida de Fluxo.")

    # Métodos de lógica
    def chegar_pedestre(self):
        if random.randint(1, 4) <= self._fluxo.value:
            pedestres = random.randint(1, 5)
            self._quantidade_pessoas += pedestres

    def atravessar(self):
        self.chegar_pedestre()
        print(f"\n🚶 {self._quantidade_pessoas} pedestres atravessaram!")
        self._quantidade_pessoas = 0
