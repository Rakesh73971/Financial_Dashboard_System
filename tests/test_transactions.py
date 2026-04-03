def test_create_transaction(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {
        "amount": 150.50,
        "type": "expense",
        "category": "software",
        "date": "2024-05-01",
        "description": "Monthly subscription"
    }
    
    response = client.post("/transactions/", json=payload, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_all_transactions(client, analyst_token):
    headers = {"Authorization": f"Bearer {analyst_token}"}
    response = client.get("/transactions/?limit=5&skip=0", headers=headers)
    
    assert response.status_code == 200
    response_data = response.json()
    assert "data" in response_data
    assert isinstance(response_data["data"], list)
    assert "total" in response_data

def test_update_transaction(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Provide ALL required fields for your TransactionCreate schema
    create_res = client.post("/transactions/", json={
        "amount": 100.0, 
        "type": "income", 
        "category": "sales",
        "date": "2024-05-01",        # Add missing required fields
        "description": "Test setup"  # Add missing required fields
    }, headers=headers)
    
    # Add this line to catch creation errors early
    assert create_res.status_code == 200, f"Creation failed: {create_res.json()}"
    
    tx_id = create_res.json()["id"]
    
    update_res = client.put(f"/transactions/{tx_id}", json={
        "amount": 200.0, 
        "type": "income", 
        "category": "sales",
        "date": "2024-05-01",
        "description": "Updated setup"
    }, headers=headers)
    
    assert update_res.status_code == 200
    assert update_res.json()["amount"] == 200.0

def test_delete_transaction(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Provide ALL required fields
    create_res = client.post("/transactions/", json={
        "amount": 50.0, 
        "type": "expense", 
        "category": "food",
        "date": "2024-05-01",
        "description": "Lunch"
    }, headers=headers)
    
    # Catch creation errors early
    assert create_res.status_code == 200, f"Creation failed: {create_res.json()}"
    
    tx_id = create_res.json()["id"]
    
    del_res = client.delete(f"/transactions/{tx_id}", headers=headers)
    assert del_res.status_code == 200