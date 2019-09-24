from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__, static_url_path='', static_folder='templates/static')

app.config['SECRET_KEY'] = 'ef2b624fc1b2a3db4defedd9a21cf33b'

posts = [
    {
        'author': 'Peter Dodu',
        'title': 'Blog Post 1',
        'Content': 'First post content',
        'date_posted': 'September 20, 2019'   
    },

      {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'Content': 'Second post content',
        'date_posted': 'September 20, 2019'   
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html', posts=posts,title='Home PeterFlask')



@app.route("/about")
def about():
    return render_template('About.html', title='About Peters Flask')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
