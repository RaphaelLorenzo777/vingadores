from datetime import datetime
from model.database import Database

class Vingador:
    lista_vingadores = []

    class categoria_vingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta-humano"
        ALIENIGENA = "Alienígena"
        DEUS = "Deus"
        ANDROIDE = "Androide"

    def __init__(self, id, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca, idequipe):
        self.id = id
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self.idequipe = idequipe
        self.convocado = False
        self.tornozeleira = False
        self.chip_gps = False

        # Adicionar automaticamente à lista de Vingadores
        Vingador.lista_vingadores.append(self)

    @staticmethod
    def carregar_herois():
        try:
            db = Database()
            db.connect()

            query = 'SELECT idheroi, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca, idequipe FROM heroi'
            herois = db.select(query)
            for heroi in herois:
                Vingador(*heroi)
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            db.disconnect()

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
    def adicionar_convocacao(motivo, data_convocacao, data_comparecimento, idheroi, status_convc):
        try:
            db = Database()
            db.connect()
 
            query = "INSERT INTO convocacao (motivo, data_convocacao, data_comparecimento, idheroi, status_convc)  VALUES (%s, %s, %s, %s, %s)"
            
            values = (motivo, data_convocacao, data_comparecimento, idheroi, status_convc)
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
 