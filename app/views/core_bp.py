from flask import Blueprint, render_template, request, flash, url_for, redirect, abort
from sqlalchemy import desc, or_

from ..models import Post

core = Blueprint('core', __name__)


@core.route('/')
def index():
    posts = Post.query.filter_by(published=True).order_by(desc(Post.created_at)).all()
    return render_template('index.html', posts=posts)


@core.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    if not post:
        abort(404)
    return render_template('post.html', post=post)


@core.route('/search', methods=['POST'])
def search():
    q = request.form['query']
    if q in ['', ' ', None]:
        flash('Invalid search!', 'error')
        return redirect(url_for('index'))

    result = Post.query.filter(Post.published == True) \
        .filter(
        or_(Post.title.contains(q), Post.body.contains(q))
    ).order_by(desc(Post.created_at)).all()
    return render_template('search.html', result=result)
