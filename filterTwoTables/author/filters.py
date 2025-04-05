import django_filters
from .models import Author, Book

class AuthorFilter(django_filters.FilterSet):
    book_title = django_filters.CharFilter(method='filter_by_book_title')

    class Meta:
        model = Author
        fields = []

    def filter_by_book_title(self, queryset, name, value):
        # Get author emails from books with matching title
        author_emails = Book.objects.filter(title=value).values_list('author_email', flat=True)
        return queryset.filter(email__in=author_emails)
