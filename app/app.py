from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def index():
    # return "¡Hola mundo!"
    misCursos = ['PHP', 'SQL Server', 'VB.Net', 'Python','Ruby']
    miData={
        'titulo': "Trabajo Academico",
        'bienvenida': "Desarrollo de Trabajo Final",
        'cursos': misCursos,
        'numero_cursos': len(misCursos)
    }
    return render_template('index.html', data= miData)


@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    miData = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad':edad
    }
    return render_template('contacto.html', data=miData)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "Ok"

def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
    
