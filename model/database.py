import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
        load_dotenv()  # Carregar as variáveis de ambiente
        self.host = getenv('BD_HOST')
        self.user = getenv('BD_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('BD_DATABASE')
        self.connection = None  # Initialize connection to None
        self.cursor = None  # Initialize cursor to None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():  # Check if the connection is successful
                self.cursor = self.connection.cursor()
                print('Conexão com o banco de dados realizada com sucesso')
        except Error as e:
            print(f'Erro: {e}')
            self.connection = None  # Set connection to None if failed
            self.cursor = None  # Set cursor to None if failed

    def disconnect(self):
        if self.connection:
            self.cursor.close()  # Close the cursor
            self.connection.close()  # Close the connection
            print('Conexão com o banco de dados encerrada com sucesso')
        else:
            print('Erro: Não há conexão aberta para fechar.')

    def execute_query(self, query, values=None):
        if not self.connection:
            print("Erro: Conexão não estabelecida. Não é possível executar a consulta.")
            return None
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print('Query executada com sucesso')
            return self.cursor
        except Error as e:
            print(f'Erro: {e}')
            return None
        
    def select(self, query):
        if not self.connection:
            print("Erro: Conexão não estabelecida. Não é possível executar a consulta.")
            return None
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro: {e}')
            return None
