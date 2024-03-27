from fastapi.testclient import TestClient
from api.v1.books import app

client = TestClient(app)


def test_create_book():
    test_data = {
        "title": "Test Book",
        "author": "Test Author",
        "publication_year": 2022
    }
    response = client.post("/books/create", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"status": True, "detail": "created successfully"}


def test_create_book_without_proper_data():
    test_data = {
        "title": "Test Book",
        "publication_year": 2022
    }
    response = client.post("/books/create", json=test_data)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [{"loc": ["body", "author"], "msg": "field required", "type": "value_error.missing"}]}


def test_submit_review():
    test_data = {
        "book_id": 1,
        "rating": 5,
        "comment": "Great book!"
    }
    response = client.post("/books/review", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"status": True, "detail": "submitted successfully"}


def test_submit_review_non_exist_book():
    test_data = {
        "book_id": 999,
        "rating": 5,
        "comment": "Great book!"
    }
    response = client.post("/books/review", json=test_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}


# Run the tests
if __name__ == "__main__":
    test_create_book()
    test_create_book_without_proper_data()
    test_submit_review()
    test_submit_review_non_exist_book()
