import sqlite3

URL_BD = 'mibd.db'

def accion(sql, datos) -> int:
    """ Se encarga de ejecutar una consulta de acción, INSERT, UPDATE, DELETE """ 
    try:
        with sqlite3.connect(URL_BD) as con: # gestor de contextos por seguridad(ordena cierre de conexion)
            cur = con.cursor()
            res = cur.execute(sql,datos).rowcount # además le pido cuantas filas fueron afectadas 
            if res!=0:
                con.commit()
    except Exception:
        res = 0
    return res

def seleccion(sql, datos) -> list:
    """ Se encarga de ejecurar una consulta de selección SELECT """ 
    try:
        with sqlite3.connect(URL_BD) as con:
            cur = con.cursor()
            res = cur.execute(sql,datos).fetchall() # muestra todos los campos
    except Exception:
        res = []
    return res