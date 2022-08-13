from __future__ import annotations

import logging

from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort

from bp_posts.dao.comment import Comment
from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from config import DATA_PATH_POST, DATA_PATH_COMMENT

# Создаем блупринт
bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")

# Создаем объекты доступа к данным
post_dao = PostDAO(DATA_PATH_POST)
comments_dao = CommentDAO(DATA_PATH_COMMENT)
api_logger = logging.getLogger("api_logger")


@bp_posts.route("/")
def page_posts_index():
    """Главная страница"""
    all_posts = post_dao.get_posts_all()
    return render_template("post_index.html", posts=all_posts)


@bp_posts.route("/posts/<int:pk>/")
def page_posts_single(pk: int):
    """Страница одного поста"""

    post: Post | None = post_dao.get_post_by_pk(pk)
    comments: list[Comment] = comments_dao.get_comments_by_post_pk(pk)

    if post is None:
        abort(404)
    api_logger.debug(pk)
    return render_template("post_single.html", post=post, comments=comments)


@bp_posts.route("/users/<user_name>")
def page_posts_by_user(user_name: str):
    """Страница пользователя"""

    posts = post_dao.get_posts_by_user(user_name)
    if not posts:
        abort(404, "Такой страницы нет")
    return render_template("post_user-feed.html", posts=posts, user_name=user_name)


@bp_posts.route("/search/")
def page_posts_search():
    """Страница поиска"""

    query: str = request.args.get("s", "")

    if query == "":
        posts: list = []
    else:
        posts: list[Post] = post_dao.search_for_posts(query)

    return render_template("post_search.html",
                           posts=posts,
                           query=query,
                           posts_len=len(posts)
                           )
