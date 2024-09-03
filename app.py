from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import pymysql as sql  # Using pymysql as the SQL library

# Function to connect to MySQL database
def sql_connect():
    conn = sql.connect(
        host="localhost",
        user="root",
        password="akshith@510",
        database="demo1"
    )
    c = conn.cursor()
    return conn, c

app = Flask(__name__)

# Route for navigation page
@app.route('/')
def nav():
    return render_template('nav.html')

# Route for menu page
@app.route('/menu')
def men():
    return render_template('menu.html')

# Route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        conn, c = sql_connect()
        try:
            c.execute("INSERT INTO pbl1 (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
        except Exception as e:
            print(f"Error inserting into pbl1: {e}")
        finally:
            c.close()
            conn.close()
        return redirect(url_for('nav'))
    return render_template('signup.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def lo():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn, c = sql_connect()
        try:
            c.execute("SELECT * FROM pbl1 WHERE username=%s and password=%s", (username, password))
            result = c.fetchone()
            if result:
                return render_template("homme.html")
            else:
                return render_template("nav.html")
        except Exception as e:
            print(f"Error during login: {e}")
        finally:
            c.close()
            conn.close()
    return render_template('login.html')

# Route for home page
@app.route('/homme')
def homm():
    return render_template('homme.html')

# Route for table reservation page
@app.route('/table', methods=['GET', 'POST'])
def res():
    if request.method == 'POST':
        customername = request.form['customername']
        tableno = request.form['tableno']
        print(customername, tableno)
        conn, c = sql_connect()
        try:
            c.execute("INSERT INTO reserve (customername, tableno) VALUES (%s, %s)", (customername, tableno))
            conn.commit()
        except Exception as e:
            print(f"Error inserting into reserve: {e}")
        finally:
            c.close()
            conn.close()
        return render_template('reee.html')
    return render_template('table.html')

# Route to serve images from the 'images' directory
@app.route('/images/<path:images>')
def serve_image(images):
    return send_from_directory("images", images)

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
