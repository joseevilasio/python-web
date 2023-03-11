
nome = "José"

palavra = ""
for letra in nome:
    
    if letra in "áéíóú":
        print("acento")
    palavra.join(letra)

print(palavra)
