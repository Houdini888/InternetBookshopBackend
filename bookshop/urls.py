# urls.py
from django.urls import path
from .views import AllBooksView

urlpatterns = [
    # Your other URL patterns go here
    path('all-books/', AllBooksView.as_view(), name='all-books'),
]
