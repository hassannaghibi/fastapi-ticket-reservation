from app.db import models


def test_get_cinemas(client, test_supercinema, supercinema_token_headers):
    response = client.get("/api/v1/cinemas", headers=supercinema_token_headers)
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": test_supercinema.id,
            "email": test_supercinema.email,
            "is_active": test_supercinema.is_active,
            "is_supercinema": test_supercinema.is_supercinema,
        }
    ]


def test_delete_cinema(client, test_supercinema, test_db, supercinema_token_headers):
    response = client.delete(
        f"/api/v1/cinemas/{test_supercinema.id}", headers=supercinema_token_headers
    )
    assert response.status_code == 200
    assert test_db.query(models.Cinema).all() == []


def test_delete_cinema_not_found(client, supercinema_token_headers):
    response = client.delete(
        "/api/v1/cinemas/4321", headers=supercinema_token_headers
    )
    assert response.status_code == 404


def test_edit_cinema(client, test_supercinema, supercinema_token_headers):
    new_cinema = {
        "email": "newemail@email.com",
        "is_active": False,
        "is_supercinema": True,
        "first_name": "Joe",
        "last_name": "Smith",
        "password": "new_password",
    }

    response = client.put(
        f"/api/v1/cinemas/{test_supercinema.id}",
        json=new_cinema,
        headers=supercinema_token_headers,
    )
    assert response.status_code == 200
    new_cinema["id"] = test_supercinema.id
    new_cinema.pop("password")
    assert response.json() == new_cinema


def test_edit_cinema_not_found(client, test_db, supercinema_token_headers):
    new_cinema = {
        "email": "newemail@email.com",
        "is_active": False,
        "is_supercinema": False,
        "password": "new_password",
    }
    response = client.put(
        "/api/v1/cinemas/1234", json=new_cinema, headers=supercinema_token_headers
    )
    assert response.status_code == 404


def test_get_cinema(
    client,
    test_cinema,
    supercinema_token_headers,
):
    response = client.get(
        f"/api/v1/cinemas/{test_cinema.id}", headers=supercinema_token_headers
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": test_cinema.id,
        "email": test_cinema.email,
        "is_active": bool(test_cinema.is_active),
        "is_supercinema": test_cinema.is_supercinema,
    }


def test_cinema_not_found(client, supercinema_token_headers):
    response = client.get("/api/v1/cinemas/123", headers=supercinema_token_headers)
    assert response.status_code == 404


def test_authenticated_cinema_me(client, cinema_token_headers):
    response = client.get("/api/v1/cinemas/me", headers=cinema_token_headers)
    assert response.status_code == 200


def test_unauthenticated_routes(client):
    response = client.get("/api/v1/cinemas/me")
    assert response.status_code == 401
    response = client.get("/api/v1/cinemas")
    assert response.status_code == 401
    response = client.get("/api/v1/cinemas/123")
    assert response.status_code == 401
    response = client.put("/api/v1/cinemas/123")
    assert response.status_code == 401
    response = client.delete("/api/v1/cinemas/123")
    assert response.status_code == 401


def test_unauthorized_routes(client, cinema_token_headers):
    response = client.get("/api/v1/cinemas", headers=cinema_token_headers)
    assert response.status_code == 403
    response = client.get("/api/v1/cinemas/123", headers=cinema_token_headers)
    assert response.status_code == 403
