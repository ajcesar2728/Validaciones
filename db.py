import sqlite3
def accion(sql, datos) -> int:
    """ Se encarga de ejecurar una consulta de acción, INSERT, UPDATE, DELETE """ 
    try:
        with sqlite3.connect('midb.db') as con:
            cur = con.cursor()
            res = cur.execute(sql,datos).rowcount
            if res!=0:
                con.commit()
    except:
        res = 0
    return res

def accion(sql, datos) -> int:
    """ Se encarga de ejecurar una consulta de acción, INSERT, UPDATE, DELETE """ 
    try:
        with sqlite3.connect('midb.db') as con:
            cur = con.cursor()
            res = cur.execute(sql,datos).rowcount
            if res!=0:
                con.commit()
    except:
        res = 0
    return res