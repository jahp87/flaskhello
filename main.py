from flask import Flask

app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola Mundo!'

@app.route('/getinstance')
def getinstance():
    return ['instance1', 'instance2', 'instance3' ]


if __name__ == '__main__':
    app.run()