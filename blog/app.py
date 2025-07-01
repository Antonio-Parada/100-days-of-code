from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post.'
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True)