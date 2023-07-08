import json 

def save_post_to_json(post):
    with open('posts.json', 'a') as file:
        json.dump(post, file)
        file.write('\n')
        
        

def load_posts_from_json():
    posts = []
    with open('posts.json', 'r') as file:
        for line in file:
            post = json.loads(line)
            post['id'] = len(posts) + 1  # Assign a unique ID to each post
            posts.append(post)
    return posts