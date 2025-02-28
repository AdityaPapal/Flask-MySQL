from  flask import Flask,jsonify
import mysql.connector

from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aditya29'
app.config['MYSQL_DB'] = 'python_connection'

mysql = MySQL(app)


@app.route('/',methods=['GET'])
def get_tables():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    data = cur.fetchall()
    cur.close()
    return str([data[0] for data in data])



if __name__ == "__main__":
    print("Connect to DB")
    app.run(debug=True)