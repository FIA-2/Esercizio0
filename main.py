from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from Flask!'

@app.route('/prova')
def index():
    return '<h1>Pagina di prova!'


app.run(host='localhost', port=3000, debug=True)

