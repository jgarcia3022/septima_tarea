from flask import Flask
from flask import request , make_response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/agregar/')
def agregar():
    return render_template('agregar.html')

@app.route('/agregado/', methods=['POST'])
def agregado() :
    if request.method == 'POST':
        palabra= request.form['palabra']
        definicion= request.form['definicion']
        resp = make_response(render_template('agregado.html'))
        resp.set_cookie('palabra',palabra)
        resp.set_cookie('definicion', definicion)
        return resp


@app.route('/ver_listado/')
def ver_listado():
    ver_cookies = request.cookies.get('palabra')
    ver_cookies2 = request.cookies.get('definicion')
    return render_template('ver_listado.html',ver_cookies=ver_cookies,ver_cookies2=ver_cookies2)

if __name__ == "__main__":
    app.run()
