from flask import Flask, request, redirect, render_template
from database import get_connection

app = Flask(__name__)


#-------------------home page-------------------
@app.route('/')
def index():
    return render_template('index.html')



#--------------------add data-------------------
@app.route("/store", methods = ["GET", "POST"])
def store():

    if request.method == "POST":

        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        mobile = request.form['mobile']
        age = request.form['age']
        gender = request.form['gender']

        conn = get_connection()
        cursor = conn.cursor()

        query = """INSERT INTO users (name, surname, email, mobile, age, gender) 
                  VALUES(%s, %s, %s, %s, %s, %s)"""


        cursor.execute(query, (name, surname, email, mobile, age, gender))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/view")

    return render_template("add_data.html")


#----------------------view data-------------------------

@app.route("/view")
def view():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    data =  cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("view_data.html", data = data)


if __name__ == "__main__":
    app.run(debug=True)