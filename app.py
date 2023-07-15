from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dao.DAOUsuario import DAOUsuario
#import mysql.connector

app = Flask(__name__)

app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()

# Define your Python list
tempV = [15, 15, 16, 16, 17, 18, 18.5, 18.7, 18.4, 19, 20, 21, 23, 25, 24, 25, 24.5, 23, 23, 22, 21, 19, 19, 17]
humeV = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
lluvV = [19, 25, 32, 25, 17, 8, 18.5, 18.7, 18.4, 19, 20.5, 21.4, 23, 25, 24, 25, 24.5, 23, 23, 22, 21, 19.8, 19, 17]
aireV = [1,2,3,5,6,1,2,8,7,6,4,3,2,1,5,6,8,9,7,8,1,0,2,5]


@app.route('/')
def index():
    return render_template('index_oficial.html')
@app.route('/acceso_pagina')
def pages_login():
    return render_template('acceso_pagina/pages-in.html')

#@app.route('/pages-in', methods=['POST', 'GET'])
#def pages_in():
#    if request.method == 'POST':
#        email = request.form.get('email')
#        password = request.form.get('password')

#        if db.check_user_credentials(email, password):
            # User exists and credentials are valid
#            return "Login successful"
#        else:
            # Invalid email or password
#            return "Invalid email or password"

#    return render_template('acceso_pagina/pages-in.html')

#@app.route('/pages-register')
#def pages_register():
#    return render_template('acceso_pagina/pages-register.html')

@app.route('/users-profile')
def users_profile():
    data = db.read(None)
    #return render_template('usuario/users-profile.html', data = data)
    if data:
        # Access the first element of the tuple
        # You can modify this line based on your data structure
        first_row = data[0]
        return render_template('usuario/users-profile.html', row=first_row)
    else:
        # Handle the case when data is empty
        return render_template('usuario/users-profile.html', row=None)

#-----------------------------------Experimental-Temperatura----------------------------------
@app.route('/Tables/Temperatura')
def table_temp():
    tempV_latest_24 = tempV[-24:]  # Get the latest 24 elements of the list
    return render_template('Tables/Temperatura.html', my_list_temp=tempV_latest_24)

# API endpoint to fetch updated values
@app.route('/api/get_values')
def get_values():
    # Update the list with new values (e.g., my_list.append('New Value'))
    # Return the updated list as a JSON response
    return jsonify(my_list)
#--------------------------------------------------------------------------------
#-----------------------------------Experimental-Lluvia----------------------------------
@app.route('/Tables/Lluvia')
def table_rain():
    lluvV_latest_24 = tempV[-24:]  # Get the latest 24 elements of the list
    return render_template('Tables/Lluvia.html', my_list_lluvia=lluvV_latest_24)

#--------------------------------------------------------------------------------
#-----------------------------------Experimental-Humedad----------------------------------
@app.route('/Tables/Humedad')
def table_hum():
    humeV_latest_24 = tempV[-24:]  # Get the latest 24 elements of the list
    return render_template('Tables/Humedad.html', my_list_hume=humeV_latest_24)

#--------------------------------------------------------------------------------
#-----------------------------------Experimental-Aire----------------------------------
@app.route('/Tables/Aire')
def table_air():
    aireV_latest_24 = tempV[-24:]  # Get the latest 24 elements of the list
    return render_template('Tables/Aire.html', my_list_aire=aireV_latest_24)

#--------------------------------------------------------------------------------


@app.route('/pages-faq')
def pages_faq():
    return render_template('ayuda/pages-faq.html')


#-----------------------------------Experimental-Register----------------------------------
@app.route('/pages-register', methods = ['POST', 'GET'])
def pages_register():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Registro satistactorio!!!")
        else:
            flash("ERROR, al registrarse")
        #return redirect(url_for('index'))
        return render_template('usuario/users-profile.html')
    else:
        #return redirect(url_for('index'))
        return render_template('acceso_pagina/pages-register.html')  
#--------------------------------------------------------------------------------

@app.route('/pages-error-404')
def pages_error_404():
    return render_template('pages-error-404.html')

if __name__ == '__main__':
    app.run()

