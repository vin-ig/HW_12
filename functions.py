import json
from pprint import pprint


def load_posts(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def search_tag(posts, tag):
    result = []
    for post in posts:
        if tag.lower() in post['content']:
            result.append(post)
    return result


# data = load_posts('posts.json')

# pprint(search_tag(data, 'вижу'))
