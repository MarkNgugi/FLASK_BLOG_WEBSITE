from flask import Flask, render_template

app = Flask(__name__)

blogs = [
    {'id':1, 'name':'DJANGO'},
    {'id':2, 'name':'SPORTS'},
    {'id':3, 'name':'EDUCATION'},
    {'id':4, 'name':'MUSIC'},
    {'id':5, 'name':'WEB DEVELOPMENT'}
]

@app.route('/home/')
def home():
    return render_template('home.html',blogs=blogs)

@app.route('/blog/<int:pk>/')
def blog(pk):
    blog = None
    for i in blogs:
        if i['id'] == int(pk):
            blog = i
    return render_template('blog.html', blogs=blog)


if __name__ == '__main__':
    app.run(debug=True)


