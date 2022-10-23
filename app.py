
from turtle import title
from flask import Flask, redirect,render_template,jsonify, url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
from sqlalchemy import desc
from cryptography.fernet import Fernet
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['QLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(500),nullable=False)
    password=db.Column(db.String(500))

    def __repr__(self) -> str:
        return f"{self.sno}&{self.username}&{self.password}"

def getLastRowId():
    con = sqlite3.connect('todo.db') 
    cur = con.cursor() 
    last_row = cur.execute('select sno from todo').fetchall()[-1]
    print(type(last_row))
    print(last_row,last_row[0])
    print(type(last_row[0]))
    return last_row[0]

def insertIntoDB(username,password):
    todo=Todo(username = username, password = password)
    db.session.add(todo)
    db.session.commit()   

    
@app.route('/login',methods=['GET','POST'])
def hello_world():
    if(request.method=="POST"):
        username=request.values.get('username')
        password=request.values.get('password')
        print(username)
        print(password)
        insertIntoDB(username,password)
        # if(getLastRowId()==12):
        return render_template('diwali.html')
    return render_template('index.html')

@app.route('/happydiwali',methods=['Get'])
def happy_diwali():
    return render_template('diwali.html')

if __name__=="__main__":
    app.run(debug=True,port=5000)
