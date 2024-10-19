from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        # Aquí procesarías los datos del formulario,
        # por ejemplo, guardarlos en una base de datos
        return "Usuario registrado con éxito!"
    return render_template('registro_usuario.html')


@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        # Aquí procesarías los datos del formulario
        return "Inscripción al curso realizada con éxito!"
    return render_template('inscripcion_curso.html')


@app.route('/registro_producto', methods=['GET', 'POST'])
def registro_producto():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        # Aquí procesarías los datos del formulario
        return "Producto registrado con éxito!"
    return render_template('registro_producto.html')


@app.route('/registro_libro', methods=['GET', 'POST'])
def registro_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        # Aquí procesarías los datos del formulario
        return "Libro registrado con éxito!"
    return render_template('registro_libro.html')


if __name__ == '__main__':
    app.run(debug=True)
