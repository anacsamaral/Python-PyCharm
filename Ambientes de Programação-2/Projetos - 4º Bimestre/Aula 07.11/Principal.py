import cherrypy
import os
from Page_especie import PaginaEspecie
localDir = os.path.dirname(__file__)


class Principal():
    topo = open("Html/cabecalho.html", encoding = 'utf-8').read()
    rodape = open("Html/rodape.html", encoding = 'utf-8').read()
    @cherrypy.expose() #exibe no navegador
    def index(self): #método index pertence a classe self para referi-se à instancia especifica da classe, acessa os atributos e métodos do objeto
        #CABEÇALHO
        html  = self.topo
        html +='''<h2>BOA NOITE ALUNINHOS</h2>'''

        #MEIO DA PÁGINA

        #RODAPÉ
        html = self.rodape

        return html
        # home = '''<h2>Olá Mundo!!!!</h2>'''
        # return '''
        # <html>
        # <head>
        # <title>Cherry Py</title>
        # </head>
        # <body>
        # <h2> Boa noite Aluninho</h2>
        # <img src ="Imagens/Unoeste.jpg" alt="Unoeste"/>
        # </body>
        # </html>'''

#criando um dicionário para colocar as informações do servidor local
server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 80
}

local_config={'/':{'tools.staticdir.on':True,
                   'tools.staticdir.dir':localDir},}

home = Principal()
home.rotaEspecie = PaginaEspecie

cherrypy.config.update(server_config)
cherrypy.quickstart(home,config=local_config)