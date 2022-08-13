from __future__ import annotations

import logging


from flask import Blueprint, jsonify
from werkzeug.exceptions import abort

from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO
from bp_posts.dao.comment_dao import CommentDAO

from config import DATA_PATH_POST, DATA_PATH_COMMENT

# Создаем блупринт
bp_api = Blueprint("bp_api", __name__)

# Создаем объекты доступа к данным
post_dao = PostDAO(DATA_PATH_POST)
comments_dao = CommentDAO(DATA_PATH_COMMENT)

api_logger = logging.getLogger("api_logger")


@bp_api.route('/posts/')
def api_posts_all():
    """Endpoint постов"""

    all_posts: list[Post] = post_dao.get_posts_all()
    all_posts_dicts: list[dict] = [post.as_dict() for post in all_posts]
    api_logger.debug("Запрошены все посты")
    return jsonify(all_posts_dicts), 200


@bp_api.route('/posts/<int:pk>/')
def api_posts_single(pk: int):
    """Endpoint одного поста"""

    post: Post | None = post_dao.get_post_by_pk(pk)

    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)

    api_logger.debug(f"Обращение к посту {pk}")
    return jsonify(post.as_dict()), 200


@bp_api.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка {error}")
    return jsonify({"error", str(error)}), 404
