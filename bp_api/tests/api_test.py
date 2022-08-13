import pytest

import main


class TestApi:
    post_keys = {"pk", "poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count"}

    @pytest.fixture
    def app_instance(self):
        app = main.app
        test_app = app.test_client()
        return test_app

    def test_posts_all_correct(self, app_instance):
        result = app_instance.get("/api/posts/")
        assert result.status_code == 200

    def test_posts_all_correct_error_keys(self, app_instance):
        result = app_instance.get("/api/posts/")
        list_or_post = result.get_json()

        for post in list_or_post:
            assert post.keys() == self.post_keys, "Неправильные ключи"

    # посты

    def test_post_correct_status(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200

    def test_post_correct_status_none(self, app_instance):
        result = app_instance.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404

    def test_post_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/")
        list_or_post = result.get_json()
        for post in list_or_post:
            assert post.keys() == self.post_keys, "Неправильные ключи"
