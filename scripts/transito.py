import random
from fluxo import Fluxo

class Transito:
    def __init__(self, tamanho_pista=15, largura_pista=2, velocidade_base=60, quantidade_inicial_carros=0, fluxo=Fluxo.BAIXO):
        self.pista = (tamanho_pista, largura_pista)
        self.quantidade_carros = quantidade_inicial_carros  # Número de carros na pista antes do semáforo
        self.velocidade_base = velocidade_base  # Velocidade limite (km/h)
        self.velocidade_media = self.velocidade_base  # Começa no limite
        self.densidade = 0  # Carros por metro
        self.fluxo = fluxo

    def calcular_densidade(self):
        self.densidade = (self.quantidade_carros//self.pista[1] ) / self.pista[0] 

    def calcular_velocidade_media(self):
        fator_congestao = max(0, 1 - self.densidade)  
        self.velocidade_media = max(10, self.velocidade_base * fator_congestao)  

    def chegar_carro(self):
        self.calcular_densidade()
        self.calcular_velocidade_media()
        fluxo_maximo =0
        if self.densidade == 0:
            fluxo_maximo = self.pista[1]  
        else:
            fluxo_maximo = max(0, int(self.velocidade_media / (self.densidade * 10)))  

        if random.randint(1, 4) <= self.fluxo.value:
            carros_chegando = min(random.randint(1, self.pista[1]), random.randint(0, fluxo_maximo))
            self.quantidade_carros += carros_chegando

    
    
    def avancar(self):
        carros_passando = random.randint(0, self.pista[1])
        self.quantidade_carros = max(0, self.quantidade_carros - carros_passando)

        print(f"\n🚗 {self.quantidade_carros} carros no total!" +
              f"\nVelocidade média: {self.velocidade_media:.1f} km/h."+
              f"\n📊 Densidade: {self.densidade:.2f} carros/m.")


    def reduzir(self):
        self.velocidade_media *= 0.5  # Reduz pela metade

    def frear(self):
        self.calcular_densidade()  # Atualiza a densidade imediatamente
        self.velocidade_media = 0


