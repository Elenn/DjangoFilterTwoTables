import django_filters
from .models import Author, Book, Department, Student

class AuthorFilter(django_filters.FilterSet):
    book_title = django_filters.CharFilter(method='filter_by_book_title')

    class Meta:
        model = Author
        fields = []

    def filter_by_book_title(self, queryset, name, value):
        # Get author emails from books with matching title
        print("a3")
        author_emails = Book.objects.filter(title=value).values_list('author_email', flat=True)
        return queryset.filter(email__in=author_emails)

class DepartmentFilter(django_filters.FilterSet):
    value = django_filters.CharFilter(method='filter_by_child_value')

    class Meta:
        model = Department
        fields = []

    def filter_by_child_value(self, queryset, name, value):
        print("a2")
        matching_codes = Student.objects.filter(value=value).values_list('code', flat=True)
        print("matching_codes", matching_codes)
        return queryset.filter(code__in=matching_codes)
