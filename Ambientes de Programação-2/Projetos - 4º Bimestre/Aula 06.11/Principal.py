import cherrypy
import os
localDir = os.path.dirname(__file__)

class Principal():
    @cherrypy.expose()  #Exibe no Navegador.
    def index(self): #Método index pertence a classe self para referir-se a instancia especifica da classe, acessa os atributos e métodos do objeto
        #home = '''<h2>Olá Mundo!</h2>'''
        return '''
        <html>
        <head>
        <title>Cherry Py</title>
        </head>
        <body>
        <h2>Boa noite Aluninho</h2>
        <img src = "Imagens/Unoeste.jpg" alt = "Unoeste"/>
        </body>
        </html> 
        '''

#Criando um dicionário para colocar as informações do servidor ideal
server_config = {
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 80
}

local_config={'/':{'tools.staticdir.on':True,
                   'tools.staticdir.dir':localDir},}

cherrypy.config.update(server_config)
cherrypy.quickstart(Principal(), config = local_config) #Inicia o servidor, padrão localhost, porta 8080 e envia uma instância de Principal()
