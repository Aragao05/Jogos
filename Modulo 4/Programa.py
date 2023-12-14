#classe mãe
class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    #salva a quantidade de likes de um programa
    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # "__str__" é um metodo especial que ordena a impressão das informações das informações da classe em um print chamando só o objeto  
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes"

#filho
class Filme(Programa): #só herda de uma classe(mãe)
    def __init__(self, nome, ano, duracao): 
        super().__init__(nome, ano) # "super()" acessa metodos de uma classe mãe 
        self.duracao = duracao

    # "__str__" é um metodo especial que ordena a impressão das informações das informações da classe em um print chamando só o objeto
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes"

#classe filho
class Serie(Programa): #só herda de uma classe(mãe)
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) # "super()" acessa metodos de uma classe mãe
        self.temporadas = temporadas
    
    # "__str__" é um metodo especial que ordena a impressão das informações das informações da classe em um print chamando só o objeto
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temp - {self.likes} likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # "__getitem__" é um metodo especial que da acesso a algumas funções de lista, como iterar, etc.
    def __getitem__(self, item):
        return self._programas[item]
    
    #"__len__" retorna a quantide de itens de um objeto
    def __len__(self):
        return len(self._programas)
    
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
interestelar = Filme("Interestelar", 2016, 200)
dark = Serie("Dark", 2014, 3)

vingadores.dar_likes()
vingadores.dar_likes()
interestelar.dar_likes()
interestelar.dar_likes()
interestelar.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
dark.dar_likes()
dark.dar_likes()
dark.dar_likes()

filmes_e_series = [vingadores, atlanta, dark, interestelar]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f"Tamanho da playlits: {len(playlist_fim_de_semana)}")