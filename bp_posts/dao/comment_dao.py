import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exceptions.data_exceptions import DataSourceError


class CommentDAO:
    """
    Загрузка json и обработка с помощью функций
    """

    def __init__(self, path):
        """
        Инициализация
        """

        self.path = path

    def _load_data(self):
        """
        Загружает из json данные
        """

        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)

        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'ошибка чтения файла джейсон {self.path}')

        return posts_data

    def _load_comments(self):
        """
        Возвращает лист с всеми комментами
        """

        comments_data = self._load_data()
        list_of_posts = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_posts

    def get_comments_by_post_pk(self, post_pk: int) -> list[Comment]:
        """
        Получает все комментарии к определенному посту по его ПК
        """

        comments: list[Comment] = self._load_comments()
        comments_match: list[Comment] = [c for c in comments if c.post_pk == post_pk]

        return comments_match


