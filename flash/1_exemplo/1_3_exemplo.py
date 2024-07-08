from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/')
def home():
    return 'Hello World'

@app.route ('/blog')
def blog():
    return render_template('blog.html', author = "Luan")

@app.route ('/blog/<string:blog_id>')
def blog_id(blog_id):
    return 'This is blog post number ' + blog_id


if __name__ == '__main__':
    app.run()