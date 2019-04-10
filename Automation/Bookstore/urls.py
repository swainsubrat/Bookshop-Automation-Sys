from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('addbook', views.add_book, name = 'addbook'),
    path('addbook_response', views.add_book_response, name = 'addbook_response'),
    path('search_book_name', views.search_book, name='search_book_name'),
    path('search_book_author', views.search_book_auth, name='search_book_author'),
    path('cart/<int:id>', views.cart_home, name = 'cart'),
    path('analytics', views.analytics, name = 'analytics'),
]