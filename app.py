from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
def users_profile():
    return render_template('users-profile.html')
if __name__=='__main__':
    app.run(debug=True,port=3001)   