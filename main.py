from flask import Flask, request, render_template

app=Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def login():
    return render_template('index.html')
 

@app.route("/verify", methods=["POST"])
def verify():
    un = request.form['username']
    pw = request.form['password']
    ver_pw = request.form['ver_password']
    email = request.form['email']

    #Process Username:
    un_error = ''
    if len(un) < 3: 
        un_error = "Username must be longer than two charaters"
    elif len(un) > 20:
        un_error = "Username must be shorter than twenty characters"
    elif ' ' in un:
        un_error = "Username must not contain spaces"
    
    #Process Password:
    pw_error= ''
    if len(pw) < 3: 
        pw_error = "Password must be longer than two charaters"
    elif len(pw) > 20:
        pw_error = "Password must be shorter than twenty characters"

    #Verify Password:
    ver_pw_error =''
    if pw != ver_pw:
        ver_pw_error = "Password and Verify Password must be the same"
    
     #Verify Email
    email_error=''
    if email == '':
        email_error = ''
    elif '@' not in email:
        email_error = "Email must contain a valid email address"

    #Check if any error
    #true route to template
    if  not un_error and not pw_error and not ver_pw_error and not email_error:
        return render_template('welcome.html', username = un)
    #false redirect to welcome page
    else:
        return render_template('index.html', 
        username = un, 
        email = email, 
        user_error = un_error,
        pass_error = pw_error,
        ver_pass_error = ver_pw_error,
        email_error = email_error)


app.run()