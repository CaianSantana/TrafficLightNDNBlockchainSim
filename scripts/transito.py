import random
import time

class Transito:
    def __init__(self):
        self.quantidade_carros = 0
        self.velocidade_media = 0

    def avancar(self):
        carros_passando = random.randint(0, 10)
        self.quantidade_carros = max(0,self.quantidade_carros-carros_passando)
        self.velocidade_media = random.randint(20, 80)  
        
        print(f"✅ VERDE: {carros_passando} carros passaram!")
        print(f"🚗 Velocidade média: {self.velocidade_media} km/h.")

    def reduzir(self):
        self.velocidade_media = 0
        print(f"⚠️ AMARELO: Carros reduzindo velocidade para {self.velocidade_media} km/h.")


    def frear(self):
        novos_carros = random.randint(5, 15)
        self.quantidade_carros += novos_carros
        print(f"🚦 VERMELHO: {novos_carros} carros chegaram! Total: {self.quantidade_carros}.")

