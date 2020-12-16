
from django.urls import path
from .views import Newspage, Home, contact, NewsDate, Register, addUser, modelform

urlpatterns = [
    path('', Home, name = 'Home'),
    path('news/', Newspage, name = 'News'),
    path('contact/', contact, name = 'contact'),
    path('newsdate/<int:year>', NewsDate, name = 'Newsdate'),
    path('register/', Register),
    path('adduser/', addUser, name='addUser'),
    path('modalform/', modelform, name='modalform'),
    path('addmodalform/', modelform, name='modalform')

]
