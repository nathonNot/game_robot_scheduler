import json
import requests


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


def act_vip():
    data = {
        "user_id":"46b0a44d-9049-4c31-9851-23dfa9b460be",
        "couponse_id":"ac7923e1-4ee4-4d60-a296-baef334f5678"
    }
    url = "http://47.102.159.15/api/couponse/activate"
    # url = "http://localhost:8000/api/couponse/activate"
    response = requests.post(url,json=data)
    print(response.text)


if __name__ == '__main__':
    act_vip()
    