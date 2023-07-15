from flask import Flask, render_template, request, redirect, url_for
import json
import post_processing

app = Flask(__name__)


@app.route('/')
def index():
    """Route renders main page template"""
    blog_posts = post_processing.all_posts()
    return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Route renders add page template with form for a new post"""
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        post_processing.add_post(author, title, content)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """Route for deleting chosen post"""
    blog_posts = post_processing.all_posts()
    for post in blog_posts:
        if post_id == post['id']:
            blog_posts.remove(post)
        json_str = json.dumps(blog_posts)
        with open("posts.json", "w") as new_file_object:
            new_file_object.write(json_str)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Route for updating chosen post"""
    # Fetch the blog posts from the JSON file
    post = post_processing.fetch_post_by_id(post_id)

    if request.method == 'POST':
        # Update the post in the JSON file
        if post['id'] == post_id:
            author = request.form.get('author')
            title = request.form.get('title')
            content = request.form.get('content')
            post_processing.update_post(post_id, author, title, content)
        # Redirect back to index
        return redirect(url_for('index'))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run()
