import random
from fluxo import Fluxo

class Transito:
    def __init__(self, tamanho_pista=15, largura_pista=2, velocidade_base=60, quantidade_inicial_carros=0, fluxo=Fluxo.BAIXO):
        self._pista = (tamanho_pista, largura_pista)
        self._quantidade_carros = quantidade_inicial_carros
        self._velocidade_base = velocidade_base
        self._velocidade_media = self._velocidade_base
        self._densidade = 0
        self._fluxo = fluxo

    # Somente leitura
    @property
    def densidade(self):
        return self._densidade

    @property
    def velocidade_media(self):
        return self._velocidade_media

    @property
    def quantidade_carros(self):
        return self._quantidade_carros

    @property
    def pista(self):
        return self._pista

    # Leitura e escrita
    @property
    def fluxo(self):
        return self._fluxo

    @fluxo.setter
    def fluxo(self, novo_fluxo):
        if isinstance(novo_fluxo, Fluxo):
            self._fluxo = novo_fluxo
        else:
            raise ValueError("⚠️ O fluxo deve ser uma instância de Fluxo.")

    @property
    def velocidade_base(self):
        return self._velocidade_base

    @velocidade_base.setter
    def velocidade_base(self, nova_velocidade):
        if isinstance(nova_velocidade, (int, float)) and nova_velocidade > 0:
            self._velocidade_base = nova_velocidade
        else:
            raise ValueError("⚠️ A velocidade base deve ser um número positivo.")

    # Métodos de lógica
    def calcular_densidade(self):
        self._densidade = (self._quantidade_carros // self._pista[1]) / self._pista[0]

    def calcular_velocidade_media(self):
        fator_congestao = max(0, 1 - self._densidade)
        self._velocidade_media = max(10, self._velocidade_base * fator_congestao)

    def chegar_carro(self):
        self.calcular_densidade()
        self.calcular_velocidade_media()
        if self._densidade == 0:
            fluxo_maximo = self._pista[1]
        else:
            fluxo_maximo = max(0, int(self._velocidade_media / (self._densidade * 10)))

        if random.randint(1, 4) <= self._fluxo.value:
            carros_chegando = min(random.randint(1, self._pista[1]), random.randint(0, fluxo_maximo))
            self._quantidade_carros += carros_chegando

    def avancar(self):
        carros_passando = random.randint(0, self._pista[1])
        self._quantidade_carros = max(0, self._quantidade_carros - carros_passando)

        print(f"\n🚗 {self._quantidade_carros} carros no total!" +
              f"\nVelocidade média: {self._velocidade_media:.1f} km/h." +
              f"\n📊 Densidade: {self._densidade:.2f} carros/m.")

    def reduzir(self):
        self._velocidade_media *= 0.5

    def frear(self):
        self.calcular_densidade()
        self._velocidade_media = 0
