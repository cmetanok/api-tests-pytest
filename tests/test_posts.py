import pytest


class TestPosts:

    def test_get_all_posts_status(self, api):
        response = api.get("/posts")
        assert response.status_code == 200

    def test_get_all_posts_not_empty(self, api):
        response = api.get("/posts")
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) > 0

    def test_get_post_by_id(self, api):
        response = api.get("/posts/1")
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 1
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)
        assert post["userId"] == 1

    def test_post_structure(self, api):
        response = api.get("/posts/1")
        post = response.json()
        expected_keys = {"id", "title", "body", "userId"}
        assert expected_keys.issubset(post.keys())

    def test_create_post(self, api):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }
        response = api.post("/posts", json=payload)
        assert response.status_code == 201
        created = response.json()
        assert created["title"] == "foo"
        assert created["body"] == "bar"
        assert created["userId"] == 1
        assert "id" in created

    def test_update_post(self, api):
        payload = {
            "id": 1,
            "title": "updated title",
            "body": "updated body",
            "userId": 1,
        }
        response = api.put("/posts/1", json=payload)
        assert response.status_code == 200
        updated = response.json()
        assert updated["title"] == "updated title"
        assert updated["body"] == "updated body"

    def test_delete_post(self, api):
        response = api.delete("/posts/1")
        assert response.status_code == 200

    @pytest.mark.parametrize("post_id", [1, 2, 3, 10, 50])
    def test_get_posts_by_ids(self, api, post_id):
        response = api.get(f"/posts/{post_id}")
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id