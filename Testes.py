class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao): 
        super().__init__(nome, ano)
        self.__duracao = duracao
       

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.temporadas if hasattr(programa,'temporadas') else (programa.duracao)
    print(f'{programa.nome} {programa.likes} {detalhes}')