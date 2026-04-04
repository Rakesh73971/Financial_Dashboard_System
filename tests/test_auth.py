def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "newuser",
        "email": "new@test.com",
        "password": "password123",
        "role": "analyst"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "new@test.com"
    assert data["username"] == "newuser"
    assert "id" in data

def test_login_user(client):
    client.post("/auth/register", json={
        "username": "loginuser",
        "email": "login@test.com",
        "password": "password123",
        "role": "admin"
    })
    response = client.post("/auth/login", data={
        "username": "login@test.com",
        "password": "password123"
    })
    assert response.status_code == 202
    assert "access_token" in response.json()