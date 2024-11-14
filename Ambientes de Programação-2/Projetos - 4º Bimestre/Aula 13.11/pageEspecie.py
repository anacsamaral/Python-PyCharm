import cherrypy
from classes.Especie import Especie
class PaginaEspecie():
    topo = open("html/cabecalho.html", encoding='utf-8').read()
    rodape = open("html/rodape.html", encoding='utf-8').read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += self.montarTabela()
        html += self.rodape
        return html

    def montarTabela(self):
        html = '''<table>
        <tr>
        <th>Código</th>
        <th>Descrição</th>
        <th>Ações</th>
        </tr>'''
    #buscar os dados do banco
        objEspecie = Especie() #Objeto do tipo especie
        dados = objEspecie.obterEspecie() #Será criado uma lista com o sql
        for linha in dados:
            html += '''<tr>
                       <td> %s</td>
                       <td> %s</td>
                       <td> [Excluir] [Alterar]</td>
                       </tr>''' %(linha['Esp_codigo'], linha['Esp_descricao'])
        html += '''</table>''' #Fechar tabela
        return html