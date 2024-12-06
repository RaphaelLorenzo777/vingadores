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

    def __init__(self, id, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca, idequipe):
        self.id = id
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_de_forca = nivel_de_forca
        self.idequipe = idequipe
        self.convocado = False
        self.tornozeleira = False
        self.chip_gps = False

        # Adicionar automaticamente à lista de Vingadores
        Vingador.lista_vingadores.append(self)

    def __str__(self):
        return f'{self.nome_heroi.ljust(20)} | {self.nome_real.ljust(20)} | {self.categoria.ljust(20)} | ' \
               f'{"Convocado" if self.convocado else "Não Convocado".ljust(20)} | ' \
               f'{"Tornozeleira Aplicada" if self.tornozeleira else "Sem Tornozeleira".ljust(20)} | ' \
               f'{"Chip GPS Aplicado" if self.chip_gps else "Sem Chip GPS".ljust(20)}'

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

    # Método para salvar convocação no banco de dados
    def convocar(self):
        if not self.convocado:
            try:
                db = Database()
                db.connect()

                data_convocacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Pega a data e hora atual
                status_convc = 'Convocado'
                
                query = '''
                    INSERT INTO convocacao (motivo, data_convocacao, data_comparecimento, status_convc,idheroi) 
                    VALUES (%s, %s, %s,%s,%s)
                '''
                db.execute_query(query, (self.id, data_convocacao, status_convc))
                self.convocado = True  # Atualiza o status_convc de convocação para True
                print(f'{self.nome_heroi} foi convocado com sucesso!')
            except Exception as e:
                print(f'Erro ao convocar: {e}')
                
            finally:
                db.disconnect()
        else:
            print(f'{self.nome_heroi} já está convocado!')

    # Método para listar as convocações
    @staticmethod
    def listar_convocacoes():
        try:
            db = Database()
            db.connect()

            query = 'SELECT c.id, h.nome_heroi, c.data_convocacao, c.status_convc FROM convocacao c JOIN heroi h ON c.idheroi = h.idheroi'
            convocacoes = db.select(query)
            
            if convocacoes:
                print(f'{"ID".ljust(5)} | {"Nome do Herói".ljust(20)} | {"Data da Convocação".ljust(20)} | {"status_convc".ljust(10)}')
                for convocacao in convocacoes:
                    print(f'{str(convocacao[0]).ljust(5)} | {convocacao[1].ljust(20)} | {convocacao[2].ljust(20)} | {convocacao[3].ljust(10)}')
            else:
                print('Não há convocações registradas.')
        except Exception as e:
            print(f'Erro ao listar convocações: {e}')
        finally:
            db.disconnect()