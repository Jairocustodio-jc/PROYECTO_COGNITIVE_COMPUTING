from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users-profile')
def users_profile():
    return render_template('usuario/users-profile.html')

if __name__ == '__main__':
    app.run()

