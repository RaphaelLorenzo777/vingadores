import os
import time
from model import vingadores
from model.vingadores import Vingador
from model.database import Database
from datetime import datetime


# Funções principais de menu
class Interface:
    animacao = True

    def __init__(self) -> None:
        Vingador.carregar_herois()
        self.menu()

    @staticmethod
    def animacaoLinhas(testiculo, duracao):
        for ch in testiculo:
            time.sleep(duracao)
            print(ch, end="", flush=True)


    @staticmethod
    def menu():
        os.system("cls")  # Limpa o console antes de exibir o menu
        if Interface.animacao:  # Apenas para a animação inicial
            Interface.animacaoLinhas(''' 


        ░█████╗░███╗░░░███╗██╗░██████╗░░█████╗░░██████╗   ██████╗░░█████╗░
        ██╔══██╗████╗░████║██║██╔════╝░██╔══██╗██╔════╝   ██╔══██╗██╔══██╗
        ███████║██╔████╔██║██║██║░░██╗░██║░░██║╚█████╗░   ██║░░██║███████║
        ██╔══██║██║╚██╔╝██║██║██║░░╚██╗██║░░██║░╚═══██╗   ██║░░██║██╔══██║
        ██║░░██║██║░╚═╝░██║██║╚██████╔╝╚█████╔╝██████╔╝   ██████╔╝██║░░██║
        ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚════╝░╚═════╝░   ╚═════╝░╚═╝░░╚═╝

            ██╗░░░██╗██╗███████╗██╗███╗░░██╗██╗░░██╗░█████╗░░█████╗░░█████╗░
            ██║░░░██║██║╚════██║██║████╗░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗
            ╚██╗░██╔╝██║░░███╔═╝██║██╔██╗██║███████║███████║██║░░╚═╝███████║
            ░╚████╔╝░██║██╔══╝░░██║██║╚████║██╔══██║██╔══██║██║░░██╗██╔══██║
            ░░╚██╔╝░░██║███████╗██║██║░╚███║██║░░██║██║░░██║╚█████╔╝██║░░██║
            ░░░╚═╝░░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
''', 0.00001)
            Interface.animacao = False
        else:
            print(''' 

        ░█████╗░███╗░░░███╗██╗░██████╗░░█████╗░░██████╗   ██████╗░░█████╗░
        ██╔══██╗████╗░████║██║██╔════╝░██╔══██╗██╔════╝   ██╔══██╗██╔══██╗
        ███████║██╔████╔██║██║██║░░██╗░██║░░██║╚█████╗░   ██║░░██║███████║
        ██╔══██║██║╚██╔╝██║██║██║░░╚██╗██║░░██║░╚═══██╗   ██║░░██║██╔══██║
        ██║░░██║██║░╚═╝░██║██║╚██████╔╝╚█████╔╝██████╔╝   ██████╔╝██║░░██║
        ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚════╝░╚═════╝░   ╚═════╝░╚═╝░░╚═╝

            ██╗░░░██╗██╗███████╗██╗███╗░░██╗██╗░░██╗░█████╗░░█████╗░░█████╗░
            ██║░░░██║██║╚════██║██║████╗░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗
            ╚██╗░██╔╝██║░░███╔═╝██║██╔██╗██║███████║███████║██║░░╚═╝███████║
            ░╚████╔╝░██║██╔══╝░░██║██║╚████║██╔══██║██╔══██║██║░░██╗██╔══██║
            ░░╚██╔╝░░██║███████╗██║██║░╚███║██║░░██║██║░░██║╚█████╔╝██║░░██║
            ░░░╚═╝░░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
''')
        print('\nSeja bem-viado! Escolha uma das opções abaixo\n')
        print("Escolha uma das opções abaixo:")
        print('1. Cadastrar vingador')
        print('2. Ver lista de vingadores ')
        print('3. Convocar vingador')
        print('4. Aplicar tornozeleira')
        print('5. Aplicar chip GPS')
        print('6. Emitir mandado de prisão')
        print('7. Sair')
 
        opcao = input("Escolha uma opção: ")

 
        if opcao == "4":
            idheroi = int(input("ID do herói: "))
            status_convc = input("status_convc (ativa/inativa): ")
            data_ativacao = input("Data de ativação (YYYY-MM-DD): ")
            data_desativacao = input("Data de desativação (YYYY-MM-DD): ")
            Vingador.adicionar_tornozeleira(idheroi, status_convc, data_ativacao, data_desativacao)
            Interface.VoltarMenu()
        elif opcao == "5":
            idheroi = int(input("ID do herói: "))
            localizacao_atual = input("Localização atual: ")
            ultima_localizacao = input("Última localização: ")
            Vingador.adicionar_chip_gps(idheroi, localizacao_atual, ultima_localizacao)
            Interface.VoltarMenu()
        elif opcao == "3":
            idheroi = int(input("ID do herói: "))
            motivo = input("Motivo da convocação: ")
            data_convocacao = input("Data da convocação (YYYY-MM-DD): ")
            data_comparecimento = input("Data do comparecimento (YYYY-MM-DD): ")
            status_convc = input("status_convc (pendente/comparecido/ausente): ")
            Vingador.adicionar_convocacao(motivo, data_convocacao, data_comparecimento, idheroi, status_convc)
            Interface.VoltarMenu()
        elif opcao == "6":
            idheroi = int(input("ID do herói: "))
            motivo = input("Motivo do mandado: ")
            data_emissao = input("Data de emissão (YYYY-MM-DD): ")
            status_convc = input("status_convc (ativo/cumprido/cancelado): ")
            Vingador.adicionar_mandado(idheroi, motivo, data_emissao, status_convc)
            Interface.VoltarMenu()
        elif opcao == "7":
            print("Saindo...")
            exit()
        elif opcao == "1":
            '''Exibe o formulário de cadastro de cada vingador e cria um novo vingador'''
            nome_heroi = input('Nome do herói: ')
            nome_real = input('Nome real: ')
            categoria = input('Categoria (Humano, Meta-humano, Androide, Deidade, Alienígena): ')

            if categoria not in [Vingador.categoria_vingadores.HUMANO, Vingador.categoria_vingadores.META_HUMANO, 
                                Vingador.categoria_vingadores.ANDROIDE, Vingador.categoria_vingadores.DEUS, 
                                Vingador.categoria_vingadores.ALIENIGENA]:
                print("Categoria inválida! Tente novamente.")
                Interface.Cadastro()
                return

            poderes = input('Poderes (separados por vírgula): ').split(",")
            poder_principal = input('Poder principal: ')
            fraquezas = input('Fraquezas (separadas por vírgula): ').split(",")
            nivel_forca = int(input('Nível de força (0 a 10000): '))

            if nivel_forca < 0 or nivel_forca > 10000:
                print("Nível de força inválido!")
                Interface.Cadastro()
                return
            
            #Salva o vingador no banco de dados
            try:
                db = Database()
                db.connect()

                query = "INSERT INTO heroi (nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca, idequipe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (nome_heroi, nome_real, categoria, ', '.join(poderes), poder_principal, ', '.join(fraquezas), nivel_forca,vingadores.idequipe)
                # nome_heroi = ';drop database vingadores;--'

                cursor = db.execute_query(query, values)
                Vingador(cursor.lastrowid, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca,vingadores.idequipe)
                Vingador.lista_vingadores.append(Vingador)
            except Exception as e:
                print(f"Erro ao salvar vingador no banco de dados: {e}")
            finally:
                db.disconnect

            print(f'Vingador {nome_heroi} cadastrado com sucesso!')
            Interface.VoltarMenu()
        elif opcao == "2":
            if not Vingador.lista_vingadores:
                print("Nenhum vingador cadastrado.")
            else:
                print(f'{"Nome do Herói".ljust(20)} | {"Nome Real".ljust(20)} | {"Categoria".ljust(20)} | '
                    f'{"Poderes".ljust(20)} | {"Poder_Principal".ljust(15)} | {"Fraquezas".ljust(25)} | '
                    f'{"Nivel_Forca".ljust(15)} | {"idequipe".ljust(17)}')
                print("=" * 180)

                for vingador in Vingador.lista_vingadores:
                    print(
                        f'{str(vingador.nome_heroi).ljust(20)} | {str(vingador.nome_real).ljust(20)} | '
                        f'{str(vingador.categoria).ljust(20)} | {str(vingador.poderes)[:20].ljust(20)} | '
                        f'{str(vingador.poder_principal)[:15].ljust(15)} | {str(vingador.fraquezas)[:25].ljust(25)} | '
                        f'{str(vingador.nivel_forca).ljust(15)} | {str(vingador.idequipe).ljust(2)}'
                    )
            Interface.VoltarMenu()
        else:
            print("Opção inválida!")
            Interface.menu()
    
    @staticmethod
    def VoltarMenu():
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls")
        Interface.menu()


    @staticmethod
    def ler_opcao_usuario(*metodos):
        opcao = input("\nDigite aqui: ")
        os.system('cls')  # Limpa o console antes de executar
        try:
            if opcao.isdigit() and 1 <= int(opcao) <= len(metodos):
                metodos[int(opcao) - 1]()
            else:
                print("Opção inválida. Tente novamente.")
                Interface.VoltarMenu()	 
        except ValueError as e:
            print(f"Erro de valor: {e}. Tente novamente.")
            Interface.VoltarMenu()
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
            Interface.VoltarMenu()
# Inicialização
# Interface.menu()