from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import Registrationform, Loginform
from flaskblog.models import User, Post


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    return render_template ('login.html', title='Login user', form = form)
