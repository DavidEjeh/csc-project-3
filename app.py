from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_clothes():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clothes (name, price, description) VALUES (%s, %s, %s)", (name, price, description))
        mysql.connection.commit()
        cur.close()
        return redirect('/view')
    return render_template('add_clothes.html')

@app.route('/view')
def view_clothes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clothes")
    data = cur.fetchall()
    cur.close()
    return render_template('view_clothes.html', clothes=data)

if __name__ == '__main__':
    app.run(debug=True)
