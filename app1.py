from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app1)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    def __repr__(self):
        return f"User('{{self.username}}','{{self.email}}')"
@app1.route('/')
def index():
    users = User.query.all()
    return render_template('index1.html', users=users)

if __name__ == '__main__':
    app1.run(debug=True)