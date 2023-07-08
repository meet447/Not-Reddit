import json

def save_comment_to_json(comment):
    with open('comments.json', 'a') as file:
        json.dump(comment, file)
        file.write('\n')
        

            
def load_comments_from_json():
    comments = []
    with open('comments.json', 'r') as file:
        for line in file:
            comment = json.loads(line)
            comments.append(comment)
    return comments