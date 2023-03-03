from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if username and password are correct
        username = request.form['username']
        password = request.form['password']
        if username == 'example' and password == 'password':
            return 'Login successful!'
        else:
            return 'Invalid login credentials'
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
