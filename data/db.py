import sqlite3

conn = sqlite3.connect('data/inventario.db')

users = [
    ('Gabriel', 'dos Passos', 'gnpassos@vitoria.es.gov.br'), 
    ('Caroline', 'de Almeida', 'carol.capini98@gmail.com'), 
    ('Rogerio', 'Luis', 'rlcalmeida@vitoria.es.gov.br'), 
    ('Mariluza', 'de Almeida', 'maalmeida@gmail.com'), 
    ('Marcide', 'Marcides', 'marcide@marcide.com'), 
    ('Angela', 'Coledetti', 'angela@angela.com')
    ]

c = conn.cursor()
#c.execute("SELECT rowid, * FROM customers")




conn.commit()
conn.close()



#sql_query = tuple((None,) + u for u in users) #SQLite entende que a ID autoincrementa quando passado Null

#c.executemany("INSERT INTO customers VALUES (?,?,?,?)", sql_query)
