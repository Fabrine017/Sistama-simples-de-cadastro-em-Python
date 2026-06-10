# Faça um mini sistema de cadastro.
lista_de_clientes = {'601' :{"Nome": "José","Idade": 30,"Telefone": "(71) 77171-7171","Email": "jose@gmail.com","Cadastro":601},
                     '602' :{"Nome": "Camila","Idade": 27,"Telefone":"(23) 22323-2323","Email": "camila@gmail.com","Cadastro":602},
                     '603' :{"Nome": "Larissa","Idade": 25,"Telefone":"(65) 66565-6565","Email": "larissa@gmail.com","Cadastro":603},
                     '604' :{"Nome": "Danilo","Idade": 29, "Telefone": "(89) 88989-8989","Email":"danilo@gmail.com","Cadastro":604}}
#Início da operação
Cadastro = len(lista_de_clientes) + 601
while True:
    print(
        f'\n---------- SISTEMA DE CADASTRO ----------\nDigite:\n1 - Cadastrar novo cliente\n2 - Listar clientes\n3 - Buscar cliente\n4 - Alterar informações\n5 - Excluir cliente\n6 - Sair')
    opçao = input('Por favor, escolha uma opção: ')
    try:
        opçao = int(opçao)
        if opçao > 6:
            raise ValueError
        #Adicionar clientes
        elif opçao == 1:
            print('Preencha os dados abaixo: ')
            Nome = input('Nome: ')
            Idade = int(input('Idade: '))
            Telefone = input('Telefone (com DDD): ')
            Email = input('Email: ')
        #Adicionando novo cliente ao dicionário "lista_de_clientes"
            lista_de_clientes[str(Cadastro)] = {'Nome': Nome,'Idade': Idade,'Telefone': Telefone,'Email':Email,'Cadastro':Cadastro}
            print(f'Número de cadastro: {Cadastro}\nNovo cliente cadastrado!')
#Listar clientes
        elif opçao == 2:
            print('Clientes cadastrados:')
            for cliente in lista_de_clientes:
                dados = lista_de_clientes[cliente]
                for tipo_de_info,info in dados.items():
                    print(f'{tipo_de_info} : {info}')
                print(f'\n')
#Buscar clientes
        elif opçao == 3:
            num_de_cadastro = input('Por favor,digite o número do cadastro: ')
            for cliente in lista_de_clientes:
                dados = lista_de_clientes[cliente]
                if num_de_cadastro == cliente:
                    for tipo_de_info,info in dados.items():
                        print(f'{tipo_de_info} : {info}')
        elif opçao == 4:
            num_de_cadastro = input('Digite o número do cadastro do cliente: ')
            tipo_de_info = input('Que informação você deseja atualizar? ').capitalize()
            atualizaçao = input(f' Digite o(a) novo(a) {tipo_de_info}: ')
            for cliente in lista_de_clientes:
                if num_de_cadastro == cliente:
                    dados = lista_de_clientes[cliente]
                    dados.update({tipo_de_info : atualizaçao})
                    print(f'\nAtualização concluída com sucesso!')
#Excluir cliente
        elif opçao == 5:
            num_de_cadastro = input('Digite o número de cadastro do cliente: ')
            dados = lista_de_clientes[num_de_cadastro]
            print(f'Essas são as informações que serão excluídas:\n')
            for tipo_de_info,info in dados.items():
                print(f'{tipo_de_info}:{info}')
            exclusao = input(f'\nDeseja continuar? (digite "sim" ou "voltar") ')
            if exclusao == 'sim':
                lista_de_clientes.pop(num_de_cadastro)
                print('Cliente excluído com sucesso!')
        else:
            print('Execução finalizada.')
            break
    except ValueError:
        print('Por favor, digite apenas números de 1 a 6.')