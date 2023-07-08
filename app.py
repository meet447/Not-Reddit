from flask import Flask, render_template, request, redirect, session
import json
import random
from Definations.comments import save_comment_to_json, load_comments_from_json
from Definations.posts import save_post_to_json, load_posts_from_json
from Definations.subreddits import save_subreddit_to_json, load_subreddits_from_json
from Definations.user import load_user_credentials, save_user_credentials

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def basic():
    return redirect("/home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = load_user_credentials()

        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/home')
        else:
            error = 'Invalid username or password.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        users = load_user_credentials()

        if username in users:
            error = 'Username already exists. Please choose a different username.'
            return render_template('register.html', error=error)

        if password != confirm_password:
            error = 'Passwords do not match. Please try again.'
            return render_template('register.html', error=error)

        users[username] = password
        save_user_credentials(users)

        session['username'] = username
        return redirect('/home')

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/create', methods=['GET'])
def index():
    posts = load_posts_from_json()
    subreddits = load_subreddits_from_json()
    subreddit_posts = {subreddit: [] for subreddit in subreddits}
    for post in posts:
        subreddit_posts[post['subreddit']].append(post)
    return render_template('create.html', subreddit_posts=subreddit_posts, subreddits=subreddits)

@app.route('/create_post', methods=['POST'])
def create_post():
    # Retrieve form data
    title = request.form.get('title')
    author = session['username'] if 'username' in session else 'Anonymous'
    content = request.form.get('content')
    subreddit = request.form.get('subreddit')
    image_url = request.form.get('image_url')  # Retrieve the image URL from the form

    post = {
        'title': title,
        'author': author,
        'content': content,
        'subreddit': subreddit,
        'likes': 1,
        'image_url': image_url  # Save the image URL in the post data
    }

    save_post_to_json(post)
    return redirect('/home')
@app.route('/create_comment', methods=['POST'])
def create_comment():
    post_id = int(request.form.get('post_id'))
    author = session['username'] if 'username' in session else 'Anonymous'
    content = request.form.get('content')

    comment = {
        'post_id': post_id,
        'author': author,
        'content': content
    }

    save_comment_to_json(comment)
    return redirect(f'/post/{post_id}')

@app.route('/post/<id>')
def post(id):
    posts = load_posts_from_json()
    comments = load_comments_from_json()
    post = next((post for post in posts if post['id'] == int(id)), None)
    post_comments = [comment for comment in comments if comment['post_id'] == int(id)]
    return render_template('post.html', post=post, comments=post_comments)

@app.route('/create_subreddit', methods=['POST'])
def create_subreddit():
    subreddit_name = request.form.get('subreddit_name')
    save_subreddit_to_json(subreddit_name)
    return redirect('/home')

@app.route('/search_subreddits', methods=['GET'])
def search_subreddits():
    search_query = request.args.get('search_query')
    subreddits = load_subreddits_from_json()
    search_results = [subreddit for subreddit in subreddits if search_query.lower() in subreddit.lower()]
    return render_template('search.html', search_results=search_results)

@app.route("/home")
def homepage():
    posts = load_posts_from_json()
    random_posts = random.sample(posts, min(10, len(posts)))  # Get a random subset of posts
    return render_template("home.html", random_posts=random_posts)

    
@app.route("/sub/<id>")
def sub(id):
    posts = load_posts_from_json()
    filtered_posts = [post for post in posts if post['subreddit'] == id]
    return render_template('subreddit.html', subreddit=id, posts=filtered_posts)

@app.route('/like_post', methods=['POST'])
def like_post():
    post_id = int(request.form.get('post_id'))
    posts = load_posts_from_json()
    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            break
    save_post_to_json(posts)
    return redirect('/home')


app.run(host='0.0.0.0')
