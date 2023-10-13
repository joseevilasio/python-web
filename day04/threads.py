import time
import concurrent.futures


def consulta_dados(): #I/O Bound
    print("Consultando dados...")
    time.sleep(2) #select no BD
    return "dados"


def processa_dados(dados): # CPU bound
    print("Processando dados...") 
    time.sleep(2) #calculando alguma coisa com os dados


def grava_log(): # I/O bound
    print("Gravando log...")
    time.sleep(2)


def main():
    start = time.perf_counter()    
    print("Inicio")

    with concurrent.futures.ThreadPoolExecutor() as executor:

        future = executor.submit(consulta_dados)
        dados = future.result()
        executor.submit(processa_dados, dados)
        executor.submit(grava_log)


    print("Fim")
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")


main()
