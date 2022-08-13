import json
from json import JSONDecodeError


from bp_posts.dao.post import Post
from exceptions.data_exceptions import DataSourceError


class PostDAO:
    """
    Загрузка из post.json и возврат в формате List
    """

    def __init__(self, path):
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

    def _load_post(self):
        """
        Возвращает лист с постами
        """
        posts_data = self._load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]
        return list_of_posts

    def get_posts_all(self):
        """
        Вернет все посты
        """
        posts = self._load_post()
        return posts

    def get_posts_by_user(self, user_name):
        """
        Загрузка поста по имени автора
        """
        posts = self._load_post()
        user_name = str(user_name).lower()
        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]
        return matching_posts

    def search_for_posts(self, query):
        """
        Загрузка поста если в нем есть данные из поиска
        """
        posts = self._load_post()
        query = str(query).lower()
        matching_posts = [post for post in posts if query in post.content.lower()]
        return matching_posts

    def get_post_by_pk(self, post_id):
        """
        Загрузка поста по РК
        """
        if type(post_id) == int:
            posts = self._load_post()
            for post in posts:
                if post.pk == post_id:
                    return post
            return

        raise TypeError("РК введено не число")
