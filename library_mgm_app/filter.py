from django_filters import FilterSet

from library_mgm_app.models import Author, Book


class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            'first_name': ['exact']
        }


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {'title': ['exact'],
                  'price': ['gt', 'lt']
                  }
