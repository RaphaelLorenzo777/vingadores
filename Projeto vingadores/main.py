from interface import Interface
from vingadores import Vingador

def main():
    Vingador('Homem de Ferro', 'Tony Stark', 'Humano', ['Inteligência', 'Engenharia', 'Rico'], 'Armadura', ['Arrogância', 'Orgulho'], 2000)
    Vingador('Capitão América', 'Steve Rogers', 'Humano', ['Força', 'Habilidade em Combate', 'Liderança'], 'Escudo', ['Inexperiência no mundo moderno'], 8000)
    Vingador('Thor', 'Thor Odinson', 'Deus', ['Força sobre-humana', 'Controle sobre raios', 'Imortalidade'], 'Mjolnir', ['Desatenção', 'Impulsividade'], 10000)
    Vingador('Hulk', 'Bruce Banner', 'Humano', ['Força sobre-humana', 'Regeneração', 'Durabilidade'], 'Força', ['Raiva', 'Controle mental'], 10000)
    Vingador('Viúva Negra', 'Natasha Romanoff', 'Humano', ['Habilidade em combate', 'Espionagem', 'Agilidade'], 'Combate corpo a corpo', ['Sem poderes sobre-humanos'], 7000)
    Vingador('Gavião Arqueiro', 'Clint Barton', 'Humano', ['Habilidade com arcos e flechas', 'Acuidade visual', 'Combate'], 'Arcos e flechas', ['Sem poderes sobre-humanos'], 6500)
    Vingador('Pantera Negra', 'T\'Challa', 'Humano', ['Força', 'Velocidade', 'Tecnologia avançada', 'Habilidades de combate'], 'Agilidade e reflexos', ['Dúvidas morais'], 9000)
    Vingador('Feiticeira Escarlate', 'Wanda Maximoff', 'Meta-humana', ['Magia', 'Manipulação de realidade', 'Telecinese'], 'Manipulação de realidade', ['Falta de controle emocional'], 10000)
    Vingador('Wolverine', 'Logan', 'Mutante', ['Regeneração', 'Força sobre-humana', 'Feras'], 'Garras de adamantium', ['Perda de controle', 'Vingança'], 9000)
    Vingador('Ciclope', 'Scott Summers', 'Mutante', ['Visão de feixe de energia', 'Habilidade estratégica'], 'Visão de feixe', ['Cegueira'], 8000)
    Vingador('Tempestade', 'Ororo Munroe', 'Mutante', ['Controle sobre o clima', 'Voo'], 'Manipulação de clima', ['Descontrole emocional'], 8000)
    Vingador('Jean Grey', 'Jean Grey', 'Mutante', ['Telepatia', 'Telecinese', 'Manipulação de energia'], 'Telecinese', ['Falta de controle sobre Phoenix'], 9500)
    Vingador('Professor X', 'Charles Xavier', 'Mutante', ['Telepatia', 'Habilidade de manipulação mental', 'Liderança'], 'Telepatia', ['Vulnerabilidade física'], 7500)
    Vingador('Fera', 'Henry McCoy', 'Mutante', ['Força sobre-humana', 'Agilidade', 'Intelecto'], 'Força física', ['Insegurança devido à aparência'], 8500)
    Vingador('Gambit', 'Remy LeBeau', 'Mutante', ['Manipulação de energia', 'Acuidade física'], 'Cartas carregadas', ['Impulsividade'], 7500)
    Vingador('Míssil', 'Rogue', 'Mutante', ['Absorção de habilidades', 'Super força', 'Invulnerabilidade'], 'Absorção de poderes', ['Perda de controle sobre os poderes'], 9000)

    Interface().menu() 

if __name__ == "__main__":
    main()
