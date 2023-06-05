from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users-profile')
def users_profile():
    return render_template('usuario/users-profile.html')

@app.route('/pages-faq')
def pages_faq():
    return render_template('ayuda/pages-faq.html')

@app.route('/pages-login')
def pages_login():
    return render_template('acceso_pagina/pages-login.html')

@app.route('/pages-register')
def pages_register():
    return render_template('acceso_pagina/pages-register.html')

@app.route('/pages-error-404')
def pages_error_404():
    return render_template('pages-error-404.html')

if __name__ == '__main__':
    app.run()

