import csv

with open('vendas.csv', mode='r', encoding='utf-8') as arquivo:
    teste_dict = csv.reader(arquivo, delimiter=",")
    for linha in teste_dict:
        print(linha)