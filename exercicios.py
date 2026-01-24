# REVISAR FUNÇÕES E ADICIONR TYPE HINTS E PYDANTIC 
#%%
from typing import List

#1 
def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

def filtrar_acima_de(valores: List[float],limite: float)-> List[float]:
    resultado =[]
    for valor in valores: 
        if valor > limite: 
            resultado.append(valor)
    return resultado 


#teste = [12,4,3,4,6,8,4,99,3,3,4,6,84,10]

#print(filtrar_acima_de(teste,10))


# 3
#%%
def contar_valores_unicos(valores: List[float])-> List[float]:
    unicos = len(set(valores))
    return unicos

# %%

def contar_valores_com_set(valores: List[float]) -> List[float]:
    return len(set(valores))
# %%

def desvio_padrao(lista: List[float]) -> List[float]:
    media = calcular_media(lista)
    variancia = sum((x - media)** 2 for x in lista) /len(lista)
    return variancia**0.5
# %%
