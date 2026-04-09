import pytest
from services.bookstore_service import BookStoreService

def test_bookstore_api_flow():
    api = BookStoreService()

    # Create User
    response = api.create_user()
    assert response.status_code == 201, f'Expected 201, but got {response.status_code}'
    userid = response.json().get('userID')
    assert userid is not None

    # Generate Token
    response = api.generate_token()
    assert response.status_code == 200
    assert api.token is not None

    # Authorized
    response = api.check_authorization()
    assert response.status_code == 200, f'Expected 200, but got {response.status_code}'

    # List books
    response = api.list_books()
    assert response.status_code == 200, f'Expected 200, but got {response.status_code}'
    books = response.json().get('books')
    assert len(books) > 0
    selected_books = [books[0]['isbn'], books[1]['isbn']]

    # Rent book
    response = api.rent_book(userid, selected_books)
    assert response.status_code == 201, f'Expected 201, but got {response.status_code}'

    # User details
    response = api.get_user_details(userid)
    assert response.status_code == 200
    user_books = response.json().get('books')
    assert len(user_books) == 2
    assert user_books[0]['isbn'] in selected_books

