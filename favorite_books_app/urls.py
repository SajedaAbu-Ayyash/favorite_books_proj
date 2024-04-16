from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index, name="index"),	 
    path('register', views.register, name= "register"),  
    path('log_in', views.log_in, name= "log_in"),
    path('addbook', views.success, name="success"),
    path('log_out', views.log_out, name= "log_out"),
    path('add_book', views.add_book, name="add_book"),
    path('addbook/<int:book_id>', views.show_book_details, name="show_book_details"),
    path('favorite_book/<int:book_id>', views.favorite_book, name="favorite_book"),
    path('update/<int:book_id>', views.edit_book, name="edit_book"),
    path('destroy/<int:book_id>', views.delete_book, name="delete_book")
    

]