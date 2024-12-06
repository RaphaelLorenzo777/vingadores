import mysql.connector
from model.database import Database
from datetime import datetime

# class Database:
#     def __init__(self):
#         self.connection = None
#         self.cursor = None
 
#     def connect(self):
#         try:
#             # Conexão com o MySQL
#             self.connection = mysql.connector.connect(
#                 host="localhost",  # Seu host (normalmente localhost)
#                 user="root",       # Seu usuário
#                 password="root",   # Sua senha
#                 database="vingadores"  # Seu banco de dados
#             )
#             self.cursor = self.connection.cursor()
#         except Exception as e:
#             print(f"Erro ao conectar ao banco de dados: {e}")
 
#     def execute_query(self, query, values=None):
#         try:
#             if values:
#                 self.cursor.execute(query, values)
#             else:
#                 self.cursor.execute(query)
#             self.connection.commit()
#             return self.cursor
#         except Exception as e:
#             print(f"Erro ao executar a query: {e}")
 
#     def select(self, query):
#         try:
#             self.cursor.execute(query)
#             return self.cursor.fetchall()
#         except Exception as e:
#             print(f"Erro ao selecionar dados: {e}")
 
#     def disconnect(self):
#         if self.connection:
#             self.connection.close()
 
# Funções para trabalhar com as novas tabelas
 
class Vingador:
    lista_vingadores = []
 
    @staticmethod
    def adicionar_tornozeleira(idheroi, status_convc, data_ativacao, data_desativacao):
        try:
            db = Database()
            db.connect()
 
            query = """INSERT INTO tornozeleira (idheroi, status_convc, data_ativacao, data_desativacao)
                       VALUES (%s, %s, %s, %s)"""
            values = (idheroi, status_convc, data_ativacao, data_desativacao)
            db.execute_query(query, values)
 
            print(f"Tornozeleira registrada com sucesso para o herói com ID {idheroi}")
        except Exception as e:
            print(f"Erro ao adicionar tornozeleira: {e}")
        finally:
            db.disconnect()
 
    @staticmethod
    def adicionar_chip_gps(idheroi, localizacao_atual, ultima_localizacao):
        try:
            db = Database()
            db.connect()
 
            query = """INSERT INTO chip_gps (idheroi, localizacao_atual, ultima_localizacao)
                       VALUES (%s, %s, %s)"""
            values = (idheroi, localizacao_atual, ultima_localizacao)
            db.execute_query(query, values)
 
            print(f"Chip GPS registrado com sucesso para o herói com ID {idheroi}")
        except Exception as e:
            print(f"Erro ao adicionar chip GPS: {e}")
        finally:
            db.disconnect()
 
    @staticmethod
    def adicionar_convocacao(motivo, data_convocacao, data_comparecimento, status_convc,idheroi):
        try:
            db = Database()
            db.connect()
 
            query = """INSERT INTO convocacao (motivo, data_convocacao, data_comparecimento, status_convc,idheroi)
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (motivo, data_convocacao, data_comparecimento, status_convc,idheroi)
            db.execute_query(query, values)
 
            print(f"Convocação registrada com sucesso para o herói com ID {idheroi}")
        except Exception as e:
            print(f"Erro ao adicionar convocação: {e}")
        finally:
            db.disconnect()
 
    @staticmethod
    def adicionar_mandado(idheroi, motivo, data_emissao, status_convc):
        try:
            db = Database()
            db.connect()
 
            query = """INSERT INTO mandado_prisao (idheroi, motivo, data_emissao, status_convc)
                       VALUES (%s, %s, %s, %s)"""
            values = (idheroi, motivo, data_emissao, status_convc)
            db.execute_query(query, values)
 
            print(f"Mandado de prisão registrado com sucesso para o herói com ID {idheroi}")
        except Exception as e:
            print(f"Erro ao adicionar mandado de prisão: {e}")
        finally:
            db.disconnect()
 
    @staticmethod
    def listar_vingadores():
        try:
            db = Database()
            db.connect()
 
            query = "SELECT idheroi, nome_heroi, nome_real FROM heroi"
            herois = db.select(query)
 
            for heroi in herois:
                print(f"ID: {heroi[0]} | Nome do Herói: {heroi[1]} | Nome Real: {heroi[2]}")
 
        except Exception as e:
            print(f"Erro ao listar os vingadores: {e}")
        finally:
            db.disconnect()
 
# Funções principais de menu
class Interface:

    def __init__(self) -> None:
        self.menu()

    @staticmethod
    def menu():
        print("Escolha uma das opções abaixo:")
        print("1. Adicionar Tornozeleira")
        print("2. Adicionar Chip GPS")
        print("3. Adicionar Convocação")
        print("4. Adicionar Mandado de Prisão")
        print("5. Listar Vingadores")
        print("6. Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            idheroi = int(input("ID do herói: "))
            status_convc = input("status_convc (ativa/inativa): ")
            data_ativacao = input("Data de ativação (YYYY-MM-DD): ")
            data_desativacao = input("Data de desativação (YYYY-MM-DD): ")
            Vingador.adicionar_tornozeleira(idheroi, status_convc, data_ativacao, data_desativacao)
        elif opcao == "2":
            idheroi = int(input("ID do herói: "))
            localizacao_atual = input("Localização atual: ")
            ultima_localizacao = input("Última localização: ")
            Vingador.adicionar_chip_gps(idheroi, localizacao_atual, ultima_localizacao)
        elif opcao == "3":
            idheroi = int(input("ID do herói: "))
            motivo = input("Motivo da convocação: ")
            data_convocacao = input("Data da convocação (YYYY-MM-DD): ")
            data_comparecimento = input("Data do comparecimento (YYYY-MM-DD): ")
            status_convc = input("status_convc (pendente/comparecido/ausente): ")
            Vingador.adicionar_convocacao(motivo, data_convocacao, data_comparecimento, status_convc,idheroi)
        elif opcao == "4":
            idheroi = int(input("ID do herói: "))
            motivo = input("Motivo do mandado: ")
            data_emissao = input("Data de emissão (YYYY-MM-DD): ")
            status_convc = input("status_convc (ativo/cumprido/cancelado): ")
            Vingador.adicionar_mandado(idheroi, motivo, data_emissao, status_convc)
        elif opcao == "5":
            Vingador.listar_vingadores()
        elif opcao == "6":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida!")
            Interface.menu()
 
# Inicialização
# Interface.menu()