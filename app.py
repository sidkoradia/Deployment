# import a library
from re import DEBUG
from flask import Flask, render_template

# instance of an app
app = Flask(__name__)

model = joblib.load('dib_79.pkl')

@app.route('/')
def welcome():
    return 'welcome'

@app.route('/homee')
def home():
    return render_template ('home.html') 

@app.route('/contact')
def contact():
    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')
    i = request.form.get('class')
    return 'hello world'

output = model.predict([a,b,c,d,e,f,g,h,i])

# run the app
if __name__ == '__main__':
    app.run(debug=True)
