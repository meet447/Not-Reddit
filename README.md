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

#File Structure

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


Certainly! Here's an example of how you can create a README file for your Not-Reddit project on GitHub:

markdown
Copy code
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
Create a virtual environment:

shell
Copy code
python3 -m venv venv
Activate the virtual environment:

For Linux/macOS:
shell
Copy code
source venv/bin/activate
For Windows:
shell
Copy code
venv\Scripts\activate
Install the dependencies:

shell
Copy code
pip install -r requirements.txt
Run the application:

shell
Copy code
flask run
Open your web browser and visit http://localhost:5000 to access the application.

File Structure
The project's file structure looks like this:

```shell
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

app.py: The main Flask application file containing the routes and logic.
templates: Directory containing HTML templates for different pages.
static: Directory containing static files such as CSS stylesheets.
users.json: JSON file storing user credentials.
posts.json: JSON file storing the posts created by users.
comments.json: JSON file storing comments on posts.
subreddits.json: JSON file storing the available subreddits.
README.md: The README file you're currently reading.