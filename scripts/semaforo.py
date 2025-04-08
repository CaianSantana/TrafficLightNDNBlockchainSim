import time
import itertools

class Semaforo:
    def __init__(self, verde=24, amarelo=3, vermelho=24,cruzamento=False):

        self.tempo_base = (verde, amarelo, vermelho)
        self.tempo_cores = {
            "VERDE": self.tempo_base[0],
            "AMARELO": self.tempo_base[1],
            "VERMELHO": self.tempo_base[2]
        }
        self.tempo_limite = tuple(t * 2 for t in self.tempo_base)
        self.ciclo_cores = itertools.cycle(self.tempo_cores.keys())
        self.cor_atual = next(self.ciclo_cores)  
        self.tempo_restante = 0
        self.cruzamento=cruzamento

    def mudar_cor(self):
        self.cor_atual = next(self.ciclo_cores)

    def alterar_tempo(self, ajuste_tempo):
        if self.cor_atual != "AMARELO":
            if isinstance(ajuste_tempo, int):
                nova_duracao = self.tempo_cores[self.cor_atual] + ajuste_tempo
                limite = self.tempo_limite[list(self.tempo_cores.keys()).index(self.cor_atual)]

                if nova_duracao <= limite:
                    self.tempo_cores[self.cor_atual] = nova_duracao
                    self.tempo_restante = max(1, self.tempo_restante + ajuste_tempo)
                    print(f"⏳ Tempo de {self.cor_atual} ajustado para {self.tempo_cores[self.cor_atual]} segundos.")
                else:
                    print(f"⛔ Tempo excederia o limite de {limite}s para a cor {self.cor_atual}.")
            else:
                print("⚠️ Ajuste de tempo inválido! Deve ser um número inteiro.")


    def contar_tempo(self):
        while True:
            self.tempo_restante = self.tempo_cores[self.cor_atual] 
            while self.tempo_restante > 0:
                print(f"\n🚦 Semáforo: {self.cor_atual} | Tempo: {self.tempo_restante}s")
                time.sleep(1)
                self.tempo_restante -= 1
            
            self.mudar_cor() 

    def avaliar(self, densidade, requisicao):
        return densidade >= requisicao

    
    def sincronizar(self, tempo, delay):
        if tempo != self.tempo_restante:
            self.tempo_restante= tempo-delay