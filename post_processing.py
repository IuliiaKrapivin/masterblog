import json


def all_posts():
    """Function uploads all posts from JSON file and returns it as a list"""
    with open("posts.json", "r") as fileobject:
        blog_posts = json.loads(fileobject.read())
    return blog_posts


def add_post(author, title, content):
    """Function takes new post data as parameters, creates
    and adds a new post to posts list and write it to the JSON file"""
    blog_posts = all_posts()
    id_list = []
    for post in blog_posts:
        id_list.append(post['id'])
    post_id = max(id_list) + 1  # assigns a unique id to new post
    new_post = {"id": post_id, "author": author, "title": title, "content": content}
    blog_posts.append(new_post)
    json_str = json.dumps(blog_posts)
    with open("posts.json", "w") as new_file_object:
        new_file_object.write(json_str)


def fetch_post_by_id(post_id):
    """Function searches for a post by an id"""
    blog_posts = all_posts()
    for post in blog_posts:
        if post_id == post['id']:
            return post


def update_post(post_id, author, title, content):
    """Function takes post data as parameters, updates post that already exist,
    writes posts list back to the JSON file"""
    blog_posts = all_posts()
    for post in blog_posts:
        if post['id'] == post_id:
            post['author'] = author
            post['title'] = title
            post['content'] = content
    json_str = json.dumps(blog_posts)
    with open("posts.json", "w") as new_file_object:
        new_file_object.write(json_str)
