from flask import Flask, render_template, request, flash
from markupsafe import escape
from db import accion, seleccion
from utils import email_valido, clave_valida
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.errorhandler(404)
def se404(e):
    return render_template("404.html")

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/registro/", methods=['GET', 'POST'])
def registro():
    if request.method=='GET':
        return render_template("registro.html", nombre='Registro')
    else:
        # 1. Recuperar los datos del formulario
        tid = escape(request.form['tidtxt'])
        nid = escape(request.form['nidtxt'])
        nom = escape(request.form['nomtxt'])
        ema = escape(request.form['ematxt'])
        usu = escape(request.form['usutxt'])
        cla = escape(request.form['clatxt'])
        ver = escape(request.form['vertxt'])
        
        # 2. Validar los datos
        swError = False
        if tid== 'NA' :
            flash('Seleccione el tipo de identificación')
            swError = True
        if nid== None or len(nid)<4 or len(nid)>40:
            flash('El número de identificación no es válido')
            swError = True
        if nom== None or len(nom)<1 or len(nom)>120:
            flash('El nombre no es válido')
            swError = True
        if ema== None or len(ema)<20 or len(ema)>120 or not email_valido(ema):
            flash('El email no es válido')
            swError = True
        if usu== None or len(usu)<8 or len(usu)>40:
            flash('El usuario no es válido')
            swError = True
        if cla== None or len(cla)<8 or len(cla)>40 or not clave_valida(cla):
            flash('La clave no es válida')
            swError = True
        if ver== None or len(ver)<8 or len(ver)>40 or not clave_valida(ver):
            flash('La verificación no es válida')
            swError = True
        if cla!=ver:
            flash('La clave y la verificación no coinciden')
            swError = True
        # 3. Ejecutar la acción
        if not swError:
            pwd = generate_password_hash(cla)
            sql = 'INSERT INTO inscritos(tid, nid, nom, ema, log, cla) VALUES(?, ?, ?, ?, ?, ?)'
            res = accion(sql, (tid, nid, nom, ema, usu, pwd))
            if res==0:
                flash("Error: los datos no se pudieron guardar!")
            else:
                flash("OK: los datos se almacenaron con éxito")
        return render_template('registro.html', nombre='Register')
            

if __name__=='__main__':
    app.run(debug=True,port=8005) 
    