from flask import Flask
from flask import MySQL

app = Flask(__name__)

mysql = MySQL()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add_contact')
def add_contact():
    return 'Add Contact'

@app.route('/edit')
def edit_contact():
    return 'edit Contact'

@app.route('/delete')
def delete_contact():
    return 'delete Contact'

if __name__ == '__main__':
    app.run(port=3000, debug=True)