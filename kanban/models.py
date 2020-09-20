from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()




class Boards(models.Model):
    class Meta:
        db_table = 'Boards'
        verbose_name = 'board'
        verbose_name_plural = 'boards'

    title = models.CharField(max_length=20, verbose_name='Board')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BoardColumns(models.Model):
    class Meta:
        db_table = 'Board_Column'
        verbose_name = 'board columns'
        verbose_name_plural = 'board column'

    board_id = models.ForeignKey(Boards, verbose_name='Board', on_delete=models.CASCADE)
    title = models.CharField(max_length=25, verbose_name='Name Column')
    create_time = models.DateTimeField(auto_now_add=True)
    sort_index = models.PositiveIntegerField(verbose_name='Sorted')

    def __str__(self):
        return self.title


class BoardCards(models.Model):
    class Meta:
        db_table = 'Board_Card'
        verbose_name = 'board cards'
        verbose_name_plural = 'board card'

    board_id = models.ForeignKey(Boards, verbose_name='Board', on_delete=models.CASCADE)
    board_column = models.ForeignKey('BoardColumns', null=True, verbose_name='Name Column', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Task')
    description = models.TextField(max_length=300, verbose_name='Description', blank=True)
    sort_index = models.PositiveIntegerField(verbose_name='Sorted')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __str__(self):
        return self.title


class BoardUser(models.Model):
    class Meta:
        db_table = 'Board_User'
        verbose_name = 'board users'
        verbose_name_plural = 'board user'

    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    board_id = models.ForeignKey(Boards, verbose_name='Board', on_delete=models.CASCADE)
    is_user = models.BooleanField(verbose_name='Do you owner')
    is_readonly = models.BooleanField(verbose_name='Read only')


class BoardUserExecutors(models.Model):
    class Meta:
        db_table = 'Board_user_executors'
        verbose_name = 'board user executor'
        verbose_name_plural = 'board user executors'

    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    card_id = models.ForeignKey(BoardCards, verbose_name='Tasks', on_delete=models.CASCADE)


class BoardCardComments(models.Model):
    class Meta:
        db_table = 'Board_card_comments'
        verbose_name = 'board card comment'
        verbose_name_plural = 'board card comments'

    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    card_id = models.ForeignKey(BoardCards, verbose_name='Tasks', on_delete=models.CASCADE)
    message = models.CharField(max_length=50, verbose_name='Message')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create Time')

    def __str__(self):
        return self.message
