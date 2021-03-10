from flask import Flask
from flask.templating import render_template 

app=Flask(__name__)

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('index.html')

@app.route('/user', methods=['POST','GET'])
def form_post():
    return render_template('user.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__=="__main__":
     app.run(debug=True)   
