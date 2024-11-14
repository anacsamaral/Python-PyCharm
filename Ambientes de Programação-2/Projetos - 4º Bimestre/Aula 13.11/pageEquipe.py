import cherrypy
class PaginaEquipe():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''<h1 class="cor">Cris e Carol</h1>'''
        html += self.rodape
        return html