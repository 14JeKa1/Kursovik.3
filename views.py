from flask import render_template, request, Blueprint
from main.posts_dao import PostsDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')
post = PostsDAO('./data/posts.json', './data/comments.json')

@main_blueprint.route('/')
def index_page():
    all_posts = posts.get_all_posts()
    return render_template('index.html', posts=all_posts)

@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    found_post = posts.get_posts_by_pk(postid)
    comments = post.get_comment_by_post_id(postid)
    return render_template('post.html',post=found_post,comments=comments)

@main_blueprint.route('/search', methods=['GET'])
def search_page():
    query = request.args.get('s')
    found_posts = post.search_post(query)
    return render_template('search.html', post=found_posts)

@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    user_posts = post.get_post_by_username(username)
    return render_template('user-feed.html', post=user_posts, username=username)