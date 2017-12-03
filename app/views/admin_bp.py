from flask import Blueprint, request, flash, render_template, url_for, redirect

from ..forms import PostForm
from ..models import Post, db

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
def dashboard():
    return render_template('admin/dashboard.html')


@admin.route('/new_post', methods=['GET', 'POST'])
def new_post():
    form = PostForm(**request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(
                title=form.title.data,
                body=form.body.data,
                published=form.publish.data)

            db.session.add(post)
            db.session.commit()
            flash('Post added successful.', 'success')
            if not post.published:
                flash('this post must be revised before published', 'info')

            return redirect(url_for('core.index'))
    return render_template('admin/new_post.html', form=form)


@admin.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm(**request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            post.title = form.title.data
            post.body = form.body.data
            post.published = form.publish.data

            db.session.add(post)
            db.session.commit()

            flash('post update successfull', 'success')
            return redirect(url_for('core.index'))
        else:
            pass

    form.title.data = post.title
    form.body.data = post.body
    form.publish.data = post.published

    return render_template('admin/edit_post.html', form=form, post_id=post.id)
