import os
from colorama import Fore, Back, Style, init
init(autoreset=True)
# gerenciamento de tarefas

lista = []

# adicionar tarefa (não adicionar tarefas com o mesmo nome)
def adicionar_tarefa():
    nome_tarefa = input('Informe o nome da tarefa: ').strip().lower()
    tarefa_existe = False

    for item in lista:
        if item['tarefa'] == nome_tarefa:
            print(f'{Fore.RED} O produto já esta cadastrado, cadastre outro ou atualize o atual.')
            tarefa_existe = True
            break

    if not tarefa_existe:
        print('Tarefa adicionada com sucesso...')
        tarefa = {'tarefa': nome_tarefa, 'status': False}
        lista.append(tarefa)
    
    
# ver tarefas
def visualizar_tarefas():
    for item in lista:
        status = item['status']
        if status:
            print(f'{Fore.GREEN}Tarefa: {item['tarefa']}\nFinalizada: Finalizada\n{'-'*20}')
        else:
            print(f'{Fore.RED}Tarefa: {item['tarefa']}\nFinalizada: Não finalizada\n{'-'*20}')


# atualizar tarefa
def atualizar_tarefa():

    tarefa = input('Informe o nome da tarefa: ')
    if any(item['tarefa'] == tarefa for item in lista):
        print('Tarefa encontrada com sucesso...')
    else:
        print('O produto informado não existe na lista...')

    if tarefa:
        for item in lista:
            if item['tarefa'] == tarefa:
                questao = input('Informe a opção desejada (1 = Nome, 2 = Alterar status)')
                if questao == '1':
                    novo_nome = input('Informe o novo nome: ')
                    item['tarefa'] = novo_nome
                else:
                    if item['status'] == False:
                        item['status'] = True
                        print('Alterado para concluido.')
                        break
                    else:
                        item['status'] = False
                        print('Alterado para Não concluido.')
                        break
            
    else:
        print('Você não preencheu o nome da tarefa...')

# deletar tarefa
def deletar():
    tarefa = input('Informe o nome da tarefa: ')
    
    if tarefa:
        for item in lista:
            if item['tarefa'] == tarefa:
                lista.remove(item)
                print('Tarefa excluida com sucesso!')
                
    else:
        print('Informe o nome da tarefa para continuar...')

print(f'{Fore.BLUE}Seja bem vindo ao gerenciador de tarefas')
while True:
    
    print(f'{Fore.YELLOW}Conforme o numero, escolha a opção desejada (informe o numero):\n\n- [1] Criar Tarefa\n- [2] Visualizar tarefas\n- [3] Atualizar Tarefa\n- [4] Deletar Tarefa\n- [5] Sair')
    opcao = input('Informe o numero da opção desejada: ')

    if opcao == '1':
        os.system('cls')
        adicionar_tarefa()
    elif opcao == '2':
        os.system('cls')
        visualizar_tarefas()
    elif opcao == '3':
        os.system('cls')
        atualizar_tarefa()
    elif opcao == '4':
        os.system('cls')
        deletar()
    elif opcao == '5':
        os.system('cls')
        print(f'{Fore.CYAN}Obrigado por utilizar o genreciador de tarefas, volte sempre!')
        break
    