from django.urls import path
from .views import *

urlpatterns = [

    path('', main),
    path('boards/', boards),
    path('boards/get_board/', BoardsList.as_view()),
    path('boards/create_board/', BoardCreate.as_view()),
    path('boards/retrieve_update_delete/<int:pk>', BoardRUD.as_view()),
    # конкретно ожидает он нас pk то есть мы сами укажим какой  id  использовать прямо в ссылке

]