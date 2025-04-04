import time
import itertools

class Semaforo:
    def __init__(self):
        self.tempo_cores = {
            "VERDE": 24,
            "AMARELO": 3,
            "VERMELHO": 24
        }
        self.ciclo_cores = itertools.cycle(self.tempo_cores.keys())
        self.corAtual = next(self.ciclo_cores)  
        self.tempo = 0

    def mudar_cor(self):
        self.corAtual = next(self.ciclo_cores)

    def alterar_tempo(self, ajuste_tempo):
        if self.corAtual !=  "AMARELO":
            if isinstance(ajuste_tempo, int):  
                self.tempo_cores[self.corAtual] += ajuste_tempo
                self.tempo = max(1, self.tempo + ajuste_tempo) 

                print(f"⏳ Tempo de {self.corAtual} ajustado para {self.tempo_cores[self.corAtual]} segundos.")
            else:
                print("⚠️ Ajuste de tempo inválido! Deve ser um número inteiro.")

    def contar_tempo(self):
        while True:
            self.tempo = self.tempo_cores[self.corAtual] 
            while self.tempo > 0:
                print(f"\n🚦 Semáforo: {self.corAtual} | Tempo: {self.tempo}s")
                time.sleep(1)
                self.tempo -= 1
            
            self.mudar_cor() 


