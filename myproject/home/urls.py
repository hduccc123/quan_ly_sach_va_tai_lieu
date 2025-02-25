
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexin,name='indexin'),
    path('list_book/', views.list_book , name ="list_book"),
    path('list_doc/', views.list_doc , name ="list_doc"),
    path('books/<int:pk>/read/', views.read_online, name='read_online'),
    path('book/',views.book_category , name="book"),
    path('doc/',views.doc_category , name = "doc"),
    path('book/<int:pk>/action/read/', views.read_book_online, name='read_book_online'), 
    path('doc/<int:pk>/action/read/', views.read_doc_online, name='read_doc_online'),
    path('login', views.login, name='login'), 
    path('register',views.register, name= 'register')
]