def test_dashboard_summary(client, analyst_token):
    headers = {"Authorization": f"Bearer {analyst_token}"}
    response = client.get("/dashboard/summary", headers=headers)
    assert response.status_code == 200

def test_dashboard_category(client, analyst_token):
    headers = {"Authorization": f"Bearer {analyst_token}"}
    response = client.get("/dashboard/category", headers=headers)
    assert response.status_code == 200

def test_dashboard_monthly(client, analyst_token):
    headers = {"Authorization": f"Bearer {analyst_token}"}
    response = client.get("/dashboard/monthly", headers=headers)
    assert response.status_code == 200

def test_dashboard_recent(client, analyst_token):
    headers = {"Authorization": f"Bearer {analyst_token}"}
    response = client.get("/dashboard/recent", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)