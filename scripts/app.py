import logging
import asyncio
from typing import Optional  # Importação do Optional
from ndn.app import NDNApp
from ndn.encoding import Name, FormalName, InterestParam, BinaryStr
import time
from semaforo import Semaforo  # Supondo que a classe Semaforo seja definida em semaforo.py

logging.basicConfig(format='[{asctime}]{levelname}:{message}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    style='{')

# Variável global INIT
INIT = True

app = NDNApp()
# Instancia os semáforos
semaforo1 = Semaforo(id=1, app=app)
semaforo2 = Semaforo(id=2, app=app)

async def main():
    global INIT  # Torna a variável INIT global dentro da função main
    try:
        # Registra os consumidores
        await semaforo1.consumer()
        await semaforo2.consumer()

        if INIT:
            await asyncio.sleep(5)  # Usando asyncio.sleep para não bloquear o loop
            INIT = False
        # Inicia os produtores de forma assíncrona
        asyncio.create_task(semaforo1.producer())  # Semáforo 1 será o produtor
        asyncio.create_task(semaforo2.producer())  # Semáforo 2 será o produtor

        # Inicia o contador de tempo para os semáforos de forma assíncrona
        asyncio.create_task(semaforo1._contar_tempo())
        asyncio.create_task(semaforo2._contar_tempo())

        # Mantém a execução do aplicativo
        await app.run_forever()

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    try:
        # Espera o loop principal iniciar e aguarda o resultado de main
        asyncio.run(main())  # Altere para asyncio.run(main()) para garantir a execução correta
    except FileNotFoundError:
        print("⛔ NFD não está rodando!")
