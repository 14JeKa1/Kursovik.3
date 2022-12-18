from utils import load_posts, get_post_by_pk

def test_load_posts():
    assert type(load_posts()) == list

espected_keys = ['poster_name','poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

def test_keys_in_load_posts():
    for post in load_posts():
        keys = [key for key in post.keys()]
        assert keys == espected_keys

def test_get_posts_by_pk():
    for i in range(1, 8):
        assert type(get_post_by_pk(i)) == dict

espected_keys = ['poster_name','poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

def test_keys_in_get_postby_pk():
    for i in range(1, 8):
        keys = [key for key in get_post_by_pk(i).keys()]
        assert keys == espected_keys
