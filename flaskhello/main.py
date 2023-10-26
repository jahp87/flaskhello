from flask import Flask

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def holamundo():
    return 'Hola Mundo!'

@app.route('/getinstance',  methods=['GET'])
def getinstance():
    print('hello')
    return ['instance1', 'instance2', 'instance3' ]


if __name__ == '__main__':
    app.run()