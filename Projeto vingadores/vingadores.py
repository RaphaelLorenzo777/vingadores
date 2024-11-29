class Vingador:
    lista_vingadores = []
    lista_poderes = [
        ""
    ]
    
    class categoria_vingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta-humano"
        ALIENIGENA = "Alienígena"
        DEUS = "Deus"
        ANDROIDE = "Androide"
    
    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_de_forca = nivel_de_forca
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

