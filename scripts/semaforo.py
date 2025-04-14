from ndn.app import NDNApp
from ndn.encoding import Name, FormalName, InterestParam, BinaryStr
from typing import Optional
import asyncio
import time
import itertools

class Semaforo:
    def __init__(self, id, app, verde=24, amarelo=3, vermelho=24, cruzamento=False):
        self.id = id
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
        self.running = True
        self._prefixo = f"/semaforo/{self.id}/status"
        self._app = app

    # Propriedades
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

    async def _contar_tempo(self):
        while self.running:
            self._tempo_restante = self._tempo_cores[self._cor_atual]
            while self._tempo_restante > 0 and self.running:
                print(f"\n🚦 {self.id} | Cor: {self._cor_atual} | Tempo restante: {self._tempo_restante}s")
                await asyncio.sleep(1)
                self._tempo_restante -= 1
            self.mudar_cor()

    async def consumer(self):
        @self._app.route(self._prefixo)
        async def on_interest(name: FormalName, param: InterestParam, _app_param: Optional[BinaryStr]):
            print(f'📥 Interesse recebido em {Name.to_str(name)}, {param}')
            
            # Exemplo de conteúdo a ser enviado de volta
            dados = {
                "id": self.id,
                "cor": self._cor_atual,
                "tempo_restante": self._tempo_restante,
            }
            content = str(dados).encode()

            await self._app.put_data(name, content=content, freshness_period=2000)
            print(f'📤 Dados enviados: {dados}')

    async def producer(self):
        while self.running:
            nome = Name.from_str(self._prefixo)
            conteudo = f"{self._cor_atual},{self._tempo_restante}".encode()
            print(f"[PRODUCER] Enviando: {Name.to_str(nome)} -> {conteudo.decode()}")

            await self._app.put_data(nome, content=conteudo, freshness_period=1000)
            
            await asyncio.sleep(1)