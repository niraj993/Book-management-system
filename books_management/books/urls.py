from django.urls import path,include
from books.views import book_list,book_update,book_delete



urlpatterns = [
    path('',book_list,name="book_list"),
    # path('create/', views.book_create, name='book_create'),
    path('book/update/<int:book_id>/', book_update, name='book_update'),
    path('book/delete/<int:book_id>/', book_delete, name='book_delete'),
] 