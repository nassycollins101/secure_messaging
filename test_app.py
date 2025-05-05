from app import app
import json

def test_login_and_post_message():
    client = app.test_client()

    # Login to get token
    res = client.post('/login', json={"username": "testuser"})
    print("Login response:", res.status_code, res.get_json())

    assert res.status_code == 200
    token = res.get_json()['token']

    # Post a message
    res2 = client.post('/messages',
                       headers={"Authorization": f"Bearer {token}"},
                       json={"message": "Hello Secure World"})
    print("Post /messages response:", res2.status_code, res2.get_json())

    assert res2.status_code == 200

# test_login_and_post_message()
# print("All tests passed ✅")