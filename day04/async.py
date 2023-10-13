import time
import asyncio


async def consulta_dados(): #I/O Bound
    print("Consultando dados...")
    await asyncio.sleep(2) #select no BD
    return "dados"


async def processa_dados(dados): # CPU bound
    print("Processando dados...") 
    await asyncio.sleep(2) #calculando alguma coisa com os dados


async def grava_log(): # I/O bound
    print("Gravando log...")
    await asyncio.sleep(2)


async def main():
    
    # dados = await consulta_dados() #Future
    # await processa_dados(dados)
    # await grava_log()

    dados = asyncio.create_task(consulta_dados())
    asyncio.create_task(processa_dados(await dados))
    asyncio.create_task(grava_log())
    

start = time.perf_counter()
print("Inicio")

asyncio.run(main()) #eventloop

print("Fim")
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")
