#    Importa a biblioteca random para gerar numeros aleatorios
import random
#    Importa a biblioteca string para usar strings comuns
import string

def CG():
    ABC = string.ascii_uppercase
    NUM = string.digits

    # Gerar os números e letras para os primeiros 5 caracteres
    FIVE = ''.join(random.choices(ABC + NUM, k=5))

    # Gerar os números para os próximos 20 caracteres
    TWE = ''.join(random.choices(NUM, k=20))

    # Formatando o código final
    END = f"{FIVE}-{TWE[0:5]}-{TWE[5:10]}-{TWE[10:15]}-{TWE[15:20]}"

    return END

# Gerar e imprimir o código
GC = CG()
print(GC)

#    Esse código foi feito por diversão escrito por Fabio Wolfgrann Junior
#    O Generator Product Activation Serial esta sob a liçensa apache 2.0