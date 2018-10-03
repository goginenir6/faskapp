from flask import Flask, render_template, url_for


app = Flask(__name__)


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
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template ('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)