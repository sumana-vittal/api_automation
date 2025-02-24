import uuid
import json
import os.path

import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def load_user_data():
    # json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    json_file_path = "/Users/raman/PycharmProjects/api_automation/data/test_data.json"
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data


def test_get_users(api_client):
    response = api_client.get("posts")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_users(api_client, load_user_data):
    # user_data={
    #     "title": "qui esse",
    #     "body": "est rerum tempore vitae",
    #     "userId": 1
    # }
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    response = api_client.post("posts", user_data)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 201
    assert len(response.json()) > 0

    response = api_client.get("posts/5")
    print(response.json())
    print(response.status_code)


def test_update_users(api_client):
    user_data={
        "title": "hellow",
        "body": "est rerum tempore vitae",
        "userId": 1
    }
    response = api_client.put("posts/1", user_data)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_delete_users(api_client):
    response = api_client.delete("posts/6")
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

