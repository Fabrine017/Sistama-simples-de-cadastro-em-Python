import json
#Funções 
def printar_informaçoes():
    for tipo_de_info,info in dados.items():
        print(f'{tipo_de_info} : {info}')

from cadastrados_json import ler_cliençoestes, cadastrar_clientes
#Início da operação
lista_de_clientes = ler_clientes()
#Prints iniciais
while True:
    print('---------- SISTEMA DE CADASTRO ----------')
    print(f'Digite:\n1 - Cadastrar novo cliente')
    print('2 - Listar clientes')
    print('3 - Buscar cliente')
    print('4 - Alterar informações')
    print('5 - Excluir cliente')
    print('6 - Sair')
    opçao = input('Por favor, escolha uma opção: ')
#Verificando número da opção
    try:
        opçao = int(opçao)
        if opçao > 6:
            raise ValueError
 #Adicionar clientes
        elif opçao == 1:
        #Coleta de dados
            print('Preencha os dados abaixo: ')
            Nome = input('Nome: ')
            Idade = int(input('Idade: '))
            Telefone = input('Telefone (com DDD): ')
            Email = input('Email: ')
        #Criando número de cadastro
            if len(lista_de_clientes) == 0:
                Cadastro = 600
            else:
                Cadastro= int(max(lista_de_clientes.keys()))+1
            print(Cadastro)
        #Adicionando clientes ao dicionário "lista_de_cliente"
            lista_de_clientes[str(Cadastro)] = {'Nome': Nome,'Idade': Idade,'Telefone': Telefone,'Email':Email,'Cadastro':Cadastro}
            cadastrar_clientes(lista_de_clientes)
            print(f'Número de cadastro: {Cadastro}\nNovo cliente cadastrado!')
#Listar clientes
        elif opçao == 2:
            print('\nIndique o modo de exibição da lista:\nR - Mais recentes primeiro\nA - Mais antigos primeiro')
            ordem = input('Em qual ordem deseja exibir? \n').upper()
            if ordem == 'A':
                print('Clientes cadastrados:\n')
                for cliente in lista_de_clientes:
                    dados = lista_de_clientes[cliente]
                    printar_informaçoes()
                    print(f'\n')
            if ordem == 'R':
                print('Clientes cadastrados:\n')
                for cliente in reversed(lista_de_clientes):
                    dados = lista_de_clientes[cliente]
                    printar_informaçoes()
                    print(f'\n')
#Buscar clientes
        elif opçao == 3:
            num_de_cadastro = input('Por favor, digite o número do cadastro: ')
            print('\n')
            for cliente in lista_de_clientes:
                dados = lista_de_clientes[cliente]
                if num_de_cadastro == cliente:
                    printar_informaçoes()
                print('\n')
#Alterar informações                        
        elif opçao == 4:
        #Coleta de informações
            num_de_cadastro = input('Digite o número do cadastro do cliente: ')
            tipo_de_info= input('Que informação você deseja atualizar? ').capitalize()
            atualizaçao = input(f'Digite o(a) novo(a) {tipo_de_info}: ')
        #Achando o ciente
            for cliente in lista_de_clientes:
                if num_de_cadastro == cliente:
                    dados = lista_de_clientes[num_de_cadastro]
        #Achando os tipos de dados do cliente e atualizando
                    dados[tipo_de_info] = atualizaçao
        #Cadastrando
                cadastrar_clientes(lista_de_clientes)
            print(f'\nAtualização concluída com sucesso!\n')
#Excluir cliente
        elif opçao == 5:
        #Coleta de informações
            num_de_cadastro = input('Digite o número de cadastro do cliente: ')
            dados = lista_de_clientes[num_de_cadastro]
        #Prints
            print(f'Essas são as informações que serão excluídas:\n')
            printar_informaçoes()
        #Exclusão
            exclusao = input(f'\nDeseja continuar? (digite "sim" ou "voltar") ')
            if exclusao == 'sim':
                lista_de_clientes.pop(num_de_cadastro)
                cadastrar_clientes(lista_de_clientes)
                print('Cliente excluído com sucesso!')
        else:
            print('Execução finalizada.')
            break
    except ValueError:
        print('Por favor, digite apenas números de 1 a 6.')