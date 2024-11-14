import sqlite3

#Conectar no banco de dados
con = sqlite3.connect("BD_Pets.db") # ou -> sqlite3.connect("d:\\BD_Pets.db")

#Criando um objeto do tipo cursor para percorrer os registros
cursor = con.cursor()

#Instrução para inserir dados
# sql = "insert into Especie (Esp_descricao) values ('Canis familiares')"
# cursor.execute(sql)
# con.commit()

# sql = "insert into Animais(Ani_nome, Ani_cor, Ani_especie) values('Pipoca', 'Caramelo', 1)"
# cursor.execute(sql)
# con.commit()

#Instrução para deletar dados
# sql = "delete from Animais where Ani_nome = 'Cristal'"
# cursor.execute(sql)
# con.commit()

#Update - atualizar os dados
# sql = "update Animais set Ani_nome = 'TOTÓ' where Ani_nome like '%Pipoca%'"
# cursor.execute(sql)
# con.commit()

#Vamos consultar e retornar em uma lista com tuplas
#fetchall - retorna uma lista
print("------------Lista de Animais--------------")
#sql = "select * from Animais"
sql = "select * from Animais, Especie where Animais.Ani_especie = Especie.Esp_cod"

cursor.execute(sql)
dados = cursor.fetchall()
for pets in dados:
    print(pets)
#con.commit()