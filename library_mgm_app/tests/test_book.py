import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db  # this used to see the play button
class TestBookEndPoint:
    def test_that_anonymous_user_cannot_get_book(self):
        response = APIClient()
        response = response.get('/library/router/books/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        # response = client.post('/library/router/books/', {"title": "a", "genre": "", "price": "", "author": 2})
        # assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_anonymous_user_cannot_create_book(self):
        response = APIClient()
        # response.post(user=User(is_staff=True))
        response = response.post(
            '/library/router/books/',
            {"title": "The man called God", "genre": "thriller", "isbn": "86367891663-32", "price": 432, "author": 1})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_that_admin_user_can_get_book(self):
    client = APIClient()
    client.force_authenticate(user=User(is_staff=True))
    response = client.get('/library/router/books/')
    assert response.status_code == status.HTTP_200_OK


def test_that_admin_user_cannot_create_book_with_bad_data(self):
    response = APIClient()
    response.force_authenticate(user=User(is_staff=True))
    response = response.post('/library/router/books/',
                             {"title": "The man called God", "genre": "thriller", "isbn": "86367891663-32",
                              "price": 432, "author": 1})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_that_admin_user_can_create_book_with_good_data(self):
    response = APIClient()
    response.force_authenticate(user=User(is_staff=True))
    response = response.post('/books/',
                             {"title": "The man called God", "description": "Best movie", "genre": "FICTION",
                              "language": "IGBO", "price": 432.45,
                              "author": "Cari Shugg", "book_number": "86367891663"})
    assert response.status_code == status.HTTP_201_CREATED

# def test_that_admin_user_can_get_400_with_invalid_data(self):
#     response = APIClient()
#     response.force_authenticate(user=User(is_staff=True))
#     response = response.post('/library/router/books/', {"title": "a", "genre": "c", "isbn":"916846781-8", "price": 428.32, "author": 2})
#     assert response.status_code == status.HTTP_400_BAD_REQUEST
