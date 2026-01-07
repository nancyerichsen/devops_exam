def test_admin_login(client):
    """Test that the admin login route is accessible."""
    response = client.post("/login", data={"id": "admin", "pw": "admin"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Admin Dashboard" in response.data