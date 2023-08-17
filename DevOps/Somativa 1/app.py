from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando um banco de dados simples em memória
class Post:
    def __init__(self, content, id):
        self.content = content
        self.id = id

posts = []

# Página inicial
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Página para adicionar um novo post
@app.route('/add', methods=['POST'])
def add_post():
    content = request.form.get('content')
    post = Post(content, len(posts))
    posts.append(post)
    return redirect(url_for('index'))

# Página para deletar um post
@app.route('/delete/<int:index>')
def delete_post(index):
    if 0 <= index < len(posts):
        del posts[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)