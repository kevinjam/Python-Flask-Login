from flask import  * 
from functools import wraps
#import the sql Library
import sqlite3


DATABASE = 'sales.db'
#render_template
app = Flask(__name__)

# From Object which look at the configuration
app.config.from_object(__name__)

app.secret_key="this kevin6734576587"

#esasey function to allow us to connect to the db
def connect_db():
   return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

#Wrapping Function
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login First')
            return redirect(url_for('log'))
    return wrap

#Logout Function goes here
# It redirect a User to the Home Page
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You are now Logout')
    return redirect(url_for('log'))

@app.route('/hello')
#`@login_required
def hello():
	g.db = connect_db()
	cur = g.db.execute('select rep_name, amount from reps')
	sales = [dict(rep_name=row[0], amount=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('hello.html', sales = sales)

@app.route('/log', methods=['GET', 'POST'])
def log():
	error = None
	if request.method =='POST':
		if request.form['username'] !='admin' or request.form['password'] !='admin':
			error='Invalid Credentials.Please try again or contact Kevin'
		else:
			session['login_in'] = True
			return redirect(url_for('hello'))
	return render_template('log.html', error=error)


if __name__ == '__main__':
	app.run(debug=True)
