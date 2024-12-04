import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv
 
class Database:
    def __init__(self):
        # Carregando variáveis de ambiente
        load_dotenv()
        self.host = getenv('BD_HOST')
        self.user = getenv('BD_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('BD_DATABASE')
        self.connection = None
        self.cursor = None
 
    def connect(self):
        """Estabelece conexão com o banco de dados"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print('Conexão com o banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Erro ao conectar ao banco de dados: {e}')
 
    def disconnect(self):
        """Encerra a conexão com o banco de dados"""
        if self.connection:
            self.connection.close()
            print('Conexão com o banco de dados encerrada com sucesso!')
 
    def execute_query(self, query, values=None):
        """Executa uma query genérica"""
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print('Query executada com sucesso!')
            return self.cursor
        except Error as e:
            print(f'Erro ao executar query: {e}')
            return None
 
    def select(self, query):
        """Executa uma query de seleção"""
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro ao executar SELECT: {e}')
            return None
 
    def atualizar_tornozeleira(self, id_tornozeleira, status):
        """Atualiza o status da tornozeleira"""
        try:
            query = """
            UPDATE tornozeleira
            SET status = %s
            WHERE idtornozeleira = %s
            """
            self.cursor.execute(query, (status, id_tornozeleira))
            self.connection.commit()
            print("Tornozeleira atualizada com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar tornozeleira: {e}")
 
    def inserir_convocacao(self, motivo, data_convocacao, status, id_heroi):
        """Insere uma nova convocação no banco de dados"""
        try:
            query = """
            INSERT INTO convocacao (motivo, data_convocacao, status, idheroi)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (motivo, data_convocacao, status, id_heroi))
            self.connection.commit()
            print("Convocação inserida com sucesso!")
        except Error as e:
            print(f"Erro ao inserir convocação: {e}")
 
 
if __name__ == "__main__":
    # Instanciando o banco
    db = Database()
    db.connect()
    db.atualizar_tornozeleira(1, "ativa")
    db.inserir_convocacao(
        "Reunião urgente",
        "2024-12-05 10:00:00",
        "pendente",
        1
    )
    db.disconnect()
 