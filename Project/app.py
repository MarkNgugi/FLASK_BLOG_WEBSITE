from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/user/')
def users():
    return render_template('blog.html')

@app.route('/room/')
def rooms():
    return render_template('room.html')

if __name__ == '__main__':
    app.run(debug=True)
