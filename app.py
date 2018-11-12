from flask import Flask, render_template, url_for
from forms import Registrationform, Loginform


app = Flask(__name__)

# app.config['SECRET_KEY'] = 'd5fa3e4e3383c1be339ef4845360ec14'


posts = [
    {
        'author': 'Ravikumar',
        'title': 'Blog post 1',
        'content': 'Hi This is first blog',
        'date_posed': 'oct 2, 2018'
    },
    {
        'author': 'anilkumar',
        'title': 'Blog post 2',
        'content': 'Hi This is secnd blog',
        'date_posed': 'oct 3, 2018'
    },
     {
        'author': 'anilkumar',
        'title': 'Blog post 2',
        'content': 'Hi This is secnd blog',
        'date_posed': 'oct 3, 2018'
    },
     {
        'author': 'anilkumar',
        'title': 'Blog post 2',
        'content': 'Hi This is secnd blog',
        'date_posed': 'oct 3, 2018'
    },
     {
        'author': 'anilkumar',
        'title': 'Blog post 2',
        'content': 'Hi This is secnd blog',
        'date_posed': 'oct 3, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template ('about.html', title='About')


@app.route('/register')
def register():
    form = Registrationform()
    return render_template ('register.html', title='register user', form = form)

@app.route('/login')
def login():
    form = Loginform()
    return render_template ('login.html', title='Login user', form = form)

if __name__ == '__main__':
    app.run(debug=True)