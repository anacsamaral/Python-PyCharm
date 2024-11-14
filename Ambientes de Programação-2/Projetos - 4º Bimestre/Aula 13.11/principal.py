import cherrypy
import os
from datetime import *
from pageEspecie import PaginaEspecie
from pageEquipe import PaginaEquipe
localDir=os.path.dirname(__file__)
class Principal():
    topo=open("html/cabecalho.html",encoding='utf-8').read()
    rodape=open("html/rodape.html",encoding='utf-8').read()
    @cherrypy.expose()#exibe no navegador
    def index(self):#o método index que pertence a classe, self para referir-se à instância específica, métodos e atributos
        #cabeçalho
        html=self.topo
        #from datetime import *
        horario=datetime.now()
        if horario.hour>0 and horario.hour<12:
            mens='Bom dia'
        elif horario.hour<18:
            mens='Boa tarde'
        else: mens='Boa noite!'
        html+='<h2>'+mens+'</h2>'
        #meio página
        html+='''<h2>Queridos Alunos!!!</h2>
                 <h1 class="cor">Aqui vai ser a página de abertura</h1>'''
        #rodapé
        html+=self.rodape
        return html

        # return '''<html>
        #           <head>
        #             <title>Aula</title>
        #           </head>
        #           <body>
        #             <h2>Boa noite!</h2>
        #             <img src="imagens/Unoeste.jpg" alt="Unoeste"/>
        #           </body>
        #           </html>'''

#vai criar um dicionário para colocar inf. do servidor
server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 81
}
cherrypy.config.update(server_config)

#criar um dicionário para encontrar os diretórios
local_config={'/':{'tools.staticdir.on':True,
                   'tools.staticdir.dir':localDir},}
home=Principal()
home.rotaEspecie=PaginaEspecie()
home.rotaEquipe=PaginaEquipe()
cherrypy.quickstart(home,config=local_config)
#neste momento ele cria um servidor local