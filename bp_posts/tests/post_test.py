import pytest as pytest

from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic",
              "content", "views_count", "likes_count", "pk"
              ]
    for field in fields:
        assert hasattr(post, field), f"Нет полей {field}"


class TestPost:

    @pytest.fixture
    def post_dao(self):
        post_dao_instant = PostDAO("data/posts.json")
        return post_dao_instant

    # Тестируем все данные

    def test_get_posts_all(self, post_dao):
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "Тип не лист"

        post = post_dao.get_posts_all()[0]
        assert type(post) == Post, "Тип не словарь"

    def test_get_all_fields(self, post_dao):
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_post_by_pk(self, post_dao):
        posts = post_dao.get_posts_all()

        correct_pk = {1, 2, 3, 4, 5, 6, 7, 8}
        pks = set([post.pk for post in posts])
        assert pks == correct_pk, "Несовпадение по ПК"

    # Тестируем по РК

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        assert type(post) == Post, "Некорректный тип результата обработки"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_post_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_post_by_pk(999)
        assert post is None, "Нет данных в ПК"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_post_by_pk(pk)
        assert post.pk == pk, "Ошибка при параметризации"

    # Тестируем функцию получения постов по имени

    def test_search_for_posts(self, post_dao):
        posts = post_dao.search_for_posts("днем")
        assert type(posts) == list, "Тип не лист"

        post = post_dao.get_posts_all()[0]
        assert type(post) == Post, "Тип не словарь"

    def test_search_for_posts_fields(self, post_dao):
        post = post_dao.get_posts_all()[0]
        check_fields(post)

    def test_search_for_posts_not_found(self, post_dao):
        posts = post_dao.search_for_posts("abirvalk")
        assert posts == [], "Пустой пост"

    @pytest.mark.parametrize("s, end_pks", [("днем", {2})])
    def test_search_for_posts_results(self, post_dao, s, end_pks):
        posts = post_dao.search_for_posts(s)
        pks = set([post.pk for post in posts])
        assert pks == end_pks, "Некорректный результат поиска"
