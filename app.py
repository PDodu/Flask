from flask import Flask, render_template, url_for, flash, redirect
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
        'author': 'Peter Dodu',
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
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))    
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    
if __name__=='__main__':
    app.run(debug=True)
