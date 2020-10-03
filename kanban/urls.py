from django.urls import path
from .views import *

urlpatterns = [

    path('', main),
    path('boards/', boards),
    path('columns/', column),
    path('cards/', card),
    path('users/', user),
    path('executors/', executor),
    path('comments/', comment),
    path('examples/', examples),


    path('examples/update/board/', test_update, name='Update_board'),
    path('examples/one/boards', test_update2, name='one_boards'),
    path('examples/list/boards', test_update3, name='list_boards'),
    path('examples/delete/boards', test_delete, name='delete_boards'),

    path('boards/get/', BoardsList.as_view(), name='get_board'),
    path('boards/get/filter/', BoardsListFilter.as_view(), name='get_board_filter'),
    path('boards/create/', BoardCreate.as_view(), name='create_board'),
    path('boards/create/connection/', BoardCreateСonnectionBoard.as_view(), name='create_board_connection_user'),
    path('boards/retrieve_update_delete/<int:pk>', BoardRUD.as_view()),
    # конкретно ожидает он нас pk то есть мы сами укажим какой  id  использовать прямо в ссылке

    path('columns/get/', BoardColumnsList.as_view(), name='get_column'),
    path('columns/create/', BoardColumnsCreate.as_view(), name='create_column'),
    path('columns/retrieve_update_delete/<int:pk>', BoardColumnsRUD.as_view()),
    path('columns/boards/<int:boards_id>', BoardColumnsFilterList.as_view()),
    path('columns/create/useboard', BoardColumnsCreateUseBoard.as_view(), name='create_column_useboard'),


    path('cards/get/', BoardCardsList.as_view(), name='get_cards'),
    path('cards/create/', BoardCardsCreate.as_view(), name='create_cards'),
    path('cards/sort/<int:board_id>', CardFilter.as_view()),
    path('cards/retrieve_update_delete/<int:pk>', BoardCardsRUD.as_view()),

    path('users/get/', BoardUserList.as_view(), name='get_users'),
    path('users/create/', BoardUserCreate.as_view(), name='get_users'),
    path('users/retrieve_update_delete/<int:pk>', BoardUserRUD.as_view()),

    path('executors/get/', BoardUserExecutorsList.as_view(), name='get_executors'),
    path('executors/create/', BoardUserExecutorsCreate.as_view(), name='get_executors'),
    path('executors/retrieve_update_delete/<int:pk>', BoardUserExecutorsRUD.as_view()),

    path('comments/get/', BoardCardCommentsList.as_view(), name='get_comments'),
    path('comments/create/', BoardCardCommentsCreate.as_view(), name='create_comments'),
    path('comments/retrieve_update_delete/<int:pk>', BoardUserExecutorsRUD.as_view()),


]
