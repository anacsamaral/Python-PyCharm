from classes.banco import Banco

class Especie():
    def __init__(self):
        self.id = 0
        self.desc = ''
        self.__banco = Banco() #Criando um projeto que acessa o banco

    #SET permite verificar ou validar o dado antes de armazenar
    def set_id(self,pid):
        if pid > 0: #Verificar se não é negativo ou zero
            self.__id = pid
    def set_desc(self,pdesc):
            self.__desc = pdesc

    #GET método para obter os valores
    def get_id(self):
        return self.__id
    def get_desc(self):
        return self.__desc

    #Devolver todas as espécies cadastradas no banco de dados
    def obterEspecie(self):
        sql = '''select Esp_Codigo,Esp_descricao from Especie order by Esp_descricao'''
        return self.__banco.executarSelect(sql)