class TestUsers:

    def test_get_all_users(self, api):
        response = api.get("/users")
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) == 10

    def test_user_structure(self, api):
        response = api.get("/users/1")
        assert response.status_code == 200
        user = response.json()
        expected_keys = {
            "id", "name", "username", "email",
            "address", "phone", "website", "company",
        }
        assert expected_keys.issubset(user.keys())

    def test_user_email_format(self, api):
        response = api.get("/users/1")
        user = response.json()
        assert "@" in user["email"]

    def test_get_user_posts(self, api):
        response = api.get("/users/1/posts")
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) > 0
        for post in posts:
            assert post["userId"] == 1