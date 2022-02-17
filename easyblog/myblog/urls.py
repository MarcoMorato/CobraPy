from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('test/', test, name='test'),
    path('content/', Content.as_view(), name='content'),
    # path('single/<int:single_id>/', single, name='single'),
    path('single/<int:pk>/', Single.as_view(), name='single'),
    path('category/<int:categories_id>', PostByCategory.as_view(), name='category'),
    path('search/', Search.as_view(), name='search'),
]
