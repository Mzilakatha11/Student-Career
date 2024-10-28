from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faculties')
def faculties():
    return render_template('faculties.html')

@app.route('/institutions')
def institutions():
    return render_template('institutions.html')

@app.route('/accounting')
def accounting():
    return render_template('accounting.html')

if __name__ == "__main__":
    app.run(debug=True)