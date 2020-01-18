from flask import Flask, render_template ,request, redirect
import sqlite3
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

def write_to_file(data):
    con = sqlite3.connect('contact.db')
    cObj = con.cursor()
    cObj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY , email TEXT ,subject TEXT ,message  TEXT ) ")
    con.commit()
    cObj.execute("INSERT INTO coin(email ,subject ,message) VALUES(? ,? ,?)" ,( data['email'] ,data['text'] ,data['message']))
    con.commit()
    cObj.close()
    con.close()

@app.route('/submitform', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/thankyou.html')
    else :
        return "something went wrong"
