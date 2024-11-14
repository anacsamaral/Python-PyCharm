import cherrypy

class PaginaEspecie():
    topo = open("Html/cabecalho.html", encoding='utf-8').read()
    rodape = open("Html/rodape.html", encoding='utf-8').read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''<h2 style = 'color: green'>PÁGINA DO BOB</h2>'''
        html += self.rodape
        return html