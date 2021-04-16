import os
from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

mysql = MySQL(config.db)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')