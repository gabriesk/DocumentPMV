import sqlite3
import pandas as pd

def createDatabase():
    conn = sqlite3.connect('data/inventario.db')
    c = conn.cursor()
    c.execute("""

        CREATE TABLE IF NOT EXISTS servidores (
        id INTEGER NOT NULL,
        matricula INTEGER NOT NULL,
        nome VARCHAR(60) NOT NULL,
        setor VARCHAR(45) NOT NULL,
        UNIQUE(matricula),
        PRIMARY KEY (id))
        """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS transferencias (
        id INTEGER NOT NULL,
        mat_remetente INTEGER NOT NULL,
        mat_destinatario INTEGER NOT NULL,
        assinado INTEGER NOT NULL,
        arquivo_endereco VARCHAR(250) NOT NULL,
        tipo text check(tipo in ("Definitivo", "Emprestimo")) NOT NULL,
        prazo DATE NULL,
        motivo VARCHAR(256) NOT NULL,
        data DATETIME NOT NULL,
        PRIMARY KEY (id),
        CONSTRAINT mat_remetente
            FOREIGN KEY (mat_remetente)
            REFERENCES servidores (id)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT mat_destinatario
            FOREIGN KEY (mat_destinatario)
            REFERENCES servidores (id)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS item_categoria (
        id INTEGER NOT NULL,
        descricao VARCHAR(45) NULL,
        PRIMARY KEY (id))
        """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS itens (
        id INTEGER NOT NULL,
        categoria INTEGER NULL,
        pat_sn VARCHAR(45) NOT NULL,
        modelo VARCHAR(45) NULL,
        fabricante VARCHAR(45) NULL,
        descricao VARCHAR(256) NULL,
        itenscol VARCHAR(45) NULL,
        PRIMARY KEY (id),
        UNIQUE (pat_sn),
        CONSTRAINT categoria
            FOREIGN KEY (categoria)
            REFERENCES item_categoria (id)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    """)
    
    c.execute("""        
        CREATE TABLE IF NOT EXISTS transferencias_itens (
        id_transferencia INTEGER NULL,
        id_item INTEGER NULL,
        CONSTRAINT id_transferencia
            FOREIGN KEY (id_transferencia)
            REFERENCES transferencias (id)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT id_item
            FOREIGN KEY (id_item)
            REFERENCES itens (id)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    """)    
    conn.commit()
    conn.close()

def dropTable(table):
    conn = sqlite3.connect('data/inventario.db')
    c = conn.cursor()
    c.execute(f"DROP TABLE {table}")
    conn.commit()
    conn.close()

def findServidor(matricula):
    conn = sqlite3.connect('data/inventario.db')
    c = conn.cursor()
    c.execute(f"SELECT * from servidores WHERE matricula = {matricula}")
    servidor = c.fetchall()
    conn.commit()
    conn.close()
    
    if servidor:    
        return servidor[0]  
    else:
        return ('', '', '-- Não encontrado --', '-- Não encontrado --')

def formatLocal(string):
    return string.replace(".","/")

def formatName(string):
    return string.title()

def updateServidores():
    conn = sqlite3.connect('data/inventario.db')
    c = conn.cursor()
    
    df = pd.read_excel('data/Servidores_Atuais.xlsx', usecols=["NOME", "LOCAL_EXERCICIO", "MATRICULA"])
    df["LOCAL_EXERCICIO"] = df["LOCAL_EXERCICIO"].apply(formatLocal)
    df["NOME"] = df["NOME"].apply(formatName)
    list = df.values.tolist()
    
    for s in list:
        try:
            s.insert(0, None)
            c.execute("INSERT INTO servidores VALUES (?,?,?,?)", s)
            print(f"Servidor {s[1]} cadastrado na base.")
    
        except sqlite3.IntegrityError:
            print(f"Servidor {s[1]} existente na base.")
    
    conn.commit()
    conn.close()
