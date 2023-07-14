from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define las rutas y las funciones controladoras
@app.route('/')
def hello_world():
    return 'Hola, mundo!'

# Inicia el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
