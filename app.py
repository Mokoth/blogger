from flask import Flask, url_for, redirect, render_template, abort

app = Flask(__name__)

posts = [
  {'id': 1, 'title': 'The Fascinating World of Street Art: From Graffiti to Murals', 'desc': 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.', 'url_img': 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80'},
  {'id': 2, 'title': 'How Art Therapy Can Help with Anxiety and Depression', 'desc': 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.', 'url_img': 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80'},
  {'id': 3, 'title': 'Exploring the Connection Between Art and Mental Health', 'desc': 'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.', 'url_img': 'https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80'}
]

@app.route('/')
def home():
  return render_template('home.html', posts = posts)

@app.route('/post/<int:post_id>')
def post(post_id):
  post = next((post for post in posts if post['id'] == post_id), None)
  if post is None:
    abort(404, description='No post with the given ID was found!')
  return render_template('post.html', post=post)

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/write')
def write():
  return render_template('write.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)