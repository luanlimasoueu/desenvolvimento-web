from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/')
def home():
    return 'Hello World'

@app.route ('/blog')
def blog():
    posts = [{'title': 'Tecnologia'}, {'title': 'Produção'},]
    return render_template('blog_3.html', author = "Luan", sunny= True, posts = posts)

@app.route ('/blog/<string:blog_id>')
def blog_id(blog_id):
    return 'This is blog post number ' + blog_id


if __name__ == '__main__':
    app.run()