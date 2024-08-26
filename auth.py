from flask import Blueprint , render_template , request , redirect , url_for , flash # message flashing
from website.models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db
from flask_login import LoginManager ,login_user , login_required,logout_user,current_user
'''
the above libraries are used to create a password using a hash function , 
it means a function which saves the password and checks if there is a match , 
but we cannot view the password that was correct
'''




auth = Blueprint('auth',__name__)

# lets now design some routes 

@auth.route('/login', methods=['GET','POST']) # url name is known as route **; method is a parameter that can be passed with the routes , GET AND POST or any variable.
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()  #gives us a user where email matches
        if user:
            if check_password_hash(user.password, password):
                flash("Logged In Successfully !" , category='success')
                login_user(user, remember=True)
                return render_template("home.html",user=current_user)
            else:
                flash('Incorrect Password , Try again ' , category="error")
                
        else:
            flash("Email does not exist ",category="error")
    '''
    data = request.form
    print(data) # gets printed in terminal ->> ImmutableMultiDict([('email', 'rehan29.ahmed11@gmail.com'), ('password', 'rehan2911')])
    
    '''
    
    return render_template("login.html" , user = current_user)

@auth.route('/logout')
@login_required # cant access until logged in
def logout():
     logout_user() # predefined function imported above
     return redirect(url_for('auth.login'))
     
     
     # return "<p> LOGOUT </p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():

    if request.method == "POST":
        email=request.form.get('email')
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email = email).first()  #gives us a user where email matches
        if user:
            flash("Email already in use ",category='erro')
        elif len(email)<4:
            flash('Email must be greater than 4 characters.' , category='error')

        elif len(firstName) < 2:
            flash('Name must be greater than 2 characters.' , category='error')
        elif password1 != password2:
            flash('Password dont match.' , category='error')
        elif len(password1) < 7:
            flash('Password is too short.', category='error')
        else:
            new_user = User(email = email , firstName = firstName , password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)

            flash("Account Created!! " , category='success')

            return redirect(url_for('views.home'))

    return render_template("signup.html",user = current_user)
