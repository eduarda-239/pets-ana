# Esse arquivo fornece conexão com o banco de dados.
import sqlite3

def conectar():
    return sqlite3.connect("patinhas.db")



# Queremos chegar em cadastrar_pet () -> SQLite -> patinhas.db -> tabela pets