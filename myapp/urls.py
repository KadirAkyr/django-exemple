from django.urls import path
from .views import *

urlpatterns = [
    # serve index.html
    path('', index, name="index"),

    #
    path('books/', BookList.as_view(), name="book-list"),
    path('books/<int:pk>/', BookDetail.as_view(), name="book-details")
]
