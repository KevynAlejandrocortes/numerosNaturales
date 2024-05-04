from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Resultado', methods=['POST'])
def resultado():
    numeros = request.form.get('numeros').split(',')
    naturales = [num for num in numeros if num.isdigit()]
    return render_template('resultado.html', naturales=naturales)

if __name__ == '__main__':
    app.run(debug=True)
    
# Como ejecutar el programa.    
# 1. para ejeucar la aplciacion abrir la terminal de visual stuido code y escribir: python app.py
# 2. abre el navegador y pon la direccion http://127.0.0.1:5000/ o http://localhost:5000/