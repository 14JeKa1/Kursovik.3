from flask import Blueprint, jsonify

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('api/posts', methods=['GET'])
def get_all_posts():
    return jsonify(load_posts())

@api_blueprint.route('api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    return jsonify(get_post_by_pk(postid))