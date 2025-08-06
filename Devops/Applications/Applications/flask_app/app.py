from flask import Flask
app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/name')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Harsha'

if __name__ == '__main__':
    app.run()