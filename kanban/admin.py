from django.contrib import admin
from .models import *


@admin.register(Boards)
class BoardsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'create_time',
    ]


@admin.register(BoardColumns)
class BoardColumnsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        # 'board_id',
        'title',
        'create_time',
        'sort_index',
    ]

@admin.register(BoardCards)
class BoardCardsAdmin(admin.ModelAdmin):
    list_display = [
        'board_id',
        'board_column',
        'title',
        'sort_index',
        'create_time',

    ]

@admin.register(BoardUser)
class BoardUserAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'board_id',
        'is_user',
        'is_readonly',
    ]


@admin.register(BoardUserExecutors)
class BoardUserExecutorsAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'card_id',
    ]


@admin.register(BoardCardComments)
class BoardCardCommentsAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'card_id',
        'message',
        'create_time'
    ]
