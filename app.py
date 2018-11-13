from flask import Flask, render_template, url_for, flash, redirect
from forms import Registrationform, Loginform


app = Flask(__name__)

app.config['SECRET_KEY'] = 'c6f224b5e9c2b5e7555558ed7ebd6346'


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

if __name__ == '__main__':
    app.run(debug=True)