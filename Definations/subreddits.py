import json

def save_subreddit_to_json(subreddit_name):
    with open('subreddits.json', 'a') as file:
        json.dump(subreddit_name, file)
        file.write('\n')
        
def load_subreddits_from_json():
    subreddits = []
    with open('subreddits.json', 'r') as file:
        for line in file:
            subreddit = json.loads(line)
            subreddits.append(subreddit)
    return subreddits