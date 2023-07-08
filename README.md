# Not Reddit

Not Reddit is a simple web application built with Flask that mimics some basic functionalities of the popular social media platform Reddit. It allows users to create posts, comment on posts, search for subreddits, and interact with the content by liking posts.

## Features

- User registration and login system
- Create, edit, and delete posts
- Comment on posts
- Search for subreddits
- Like posts
- Responsive design for mobile and desktop

## Installation

1. Clone the repository:
```shell
   git clone https://github.com/your-username/not-reddit.git
   cd not-reddit
   ```

2. Create a virtual environment:
```shell
   git clone https://github.com/your-username/not-reddit.git
   cd not-reddit
   ```
3. Activate the virtual environment:

   For Linux/macOS:
```shell
    source venv/bin/activate
```
For Windows:

```shell
    venv\Scripts\activate
```
4.  Run Application:

```shell
flask run
```

5. Open your web browser and visit http://localhost:5000 to access the application.

# File Structure

```python
├── app.py
├── templates
│   ├── base.html
│   ├── create.html
│   ├── home.html
│   ├── login.html
│   ├── post.html
│   ├── register.html
│   └── subreddit.html
├── static
│   └── main.css
├── users.json
├── posts.json
├── comments.json
├── subreddits.json
└── README.md
```


