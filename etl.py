import csv 

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str)-> list[dict]:
    """ler um csv e retornar uma lista de dicionários """

    lista =[]
    with open(nome_do_arquivo_csv, mode="r", encoding ='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha) 
    return lista

def filtrar_produtos_por_categoria(lista: list[dict], categoria: str) -> list[dict]:
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("Categoria") == categoria:
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict])-> int:
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("Venda"))
    return valor_total



lista_de_produtos = ler_csv(path_arquivo)

# Filtrar produtos da categoria Electronics
produtos_filtrados = filtrar_produtos_por_categoria(lista_de_produtos, "Electronics")

valor_dos_produtos_filtrados = somar_valores_dos_produtos(produtos_filtrados)

print(f"Produtos filtrados: {produtos_filtrados}")
print(f"Valor total dos produtos: {valor_dos_produtos_filtrados}")