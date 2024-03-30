from django.urls import path, include
from app.views import home, book_list, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('api-auth/', include('rest_framework.urls')),
]