from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/quest_sheet/')
def quest_sheet():
    return 'quest sheet'

if __name__ == '__main__':
    app.run(debug=True)