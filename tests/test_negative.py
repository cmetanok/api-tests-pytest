class TestNegative:

    def test_get_nonexistent_post(self, api):
        response = api.get("/posts/9999")
        assert response.status_code == 404

    def test_get_nonexistent_endpoint(self, api):
        response = api.get("/nonexistent-endpoint")
        assert response.status_code == 404

    def test_post_empty_body(self, api):
        response = api.post("/posts", json={})
        assert response.status_code == 201

    def test_invalid_method(self, api):
        response = api.patch("/posts/1", json={"title": "patched"})
        assert response.status_code == 200