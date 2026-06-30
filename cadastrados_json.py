import json
#Ler o arquivo
def ler_clientes():
    try:
        with open ('cadastrados.json','r') as clientes:
            return json.load(clientes)
    except FileNotFoundError:
        return ()

#Cdastrar clientes
def cadastrar_clientes(lista_de_clientes):
    with open ('cadastrados.json', 'w') as clientes:
        json.dump(lista_de_clientes,clientes,indent=4)