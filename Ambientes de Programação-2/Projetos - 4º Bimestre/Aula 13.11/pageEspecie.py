import cherrypy
class PaginaEspecie():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''<h2>colocar o formulário e uma tabela para exibir as espécies</h2>'''
        html += self.rodape
        return html
