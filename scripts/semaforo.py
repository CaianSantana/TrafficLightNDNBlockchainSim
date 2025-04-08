import time
import itertools

class Semaforo:
    def __init__(self, verde=24, amarelo=3, vermelho=24, cruzamento=False):
        self._tempo_base = (verde, amarelo, vermelho)
        self._tempo_cores = {
            "VERDE": self._tempo_base[0],
            "AMARELO": self._tempo_base[1],
            "VERMELHO": self._tempo_base[2]
        }
        self._tempo_limite = tuple(t * 2 for t in self._tempo_base)
        self._ciclo_cores = itertools.cycle(self._tempo_cores.keys())
        self._cor_atual = next(self._ciclo_cores)
        self._tempo_restante = 0
        self._cruzamento = cruzamento

    # Propriedades de leitura
    @property
    def tempo_cores(self):
        return self._tempo_cores.copy()

    @property
    def tempo_restante(self):
        return self._tempo_restante

    @property
    def cor_atual(self):
        return self._cor_atual

    @property
    def cruzamento(self):
        return self._cruzamento

    def mudar_cor(self):
        self._cor_atual = next(self._ciclo_cores)

    def alterar_tempo(self, ajuste_tempo):
        if self._cor_atual != "AMARELO":
            if isinstance(ajuste_tempo, int):
                nova_duracao = self._tempo_cores[self._cor_atual] + ajuste_tempo
                limite = self._tempo_limite[list(self._tempo_cores.keys()).index(self._cor_atual)]

                if nova_duracao <= limite:
                    self._tempo_cores[self._cor_atual] = nova_duracao
                    self._tempo_restante = max(1, self._tempo_restante + ajuste_tempo)
                    print(f"⏳ Tempo de {self._cor_atual} ajustado para {self._tempo_cores[self._cor_atual]} segundos.")
                else:
                    print(f"⛔ Tempo excederia o limite de {limite}s para a cor {self._cor_atual}.")
            else:
                print("⚠️ Ajuste de tempo inválido! Deve ser um número inteiro.")

    def contar_tempo(self):
        while True:
            self._tempo_restante = self._tempo_cores[self._cor_atual]
            while self._tempo_restante > 0:
                print(f"\n🚦 Semáforo: {self._cor_atual} | Tempo: {self._tempo_restante}s")
                time.sleep(1)
                self._tempo_restante -= 1

            self.mudar_cor()

    def avaliar(self, densidade, requisicao):
        return densidade >= requisicao

    def sincronizar(self, tempo, delay):
        if tempo != self._tempo_restante:
            self._tempo_restante = tempo - delay
