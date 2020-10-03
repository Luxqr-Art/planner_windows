from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, filters, permissions, status, response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import *

def main(request):
    return render(request, 'base.html')


def boards(request):
    return render(request, 'board.html')


def column(request):
    return render(request, 'column.html')


def card(request):
    return render(request, 'cards.html')


def user(request):
    return render(request, 'user.html')


def executor(request):
    return render(request, 'executor.html')


def comment(request):
    return render(request, 'comment.html')


def examples(request):
    return render(request, 'Examples.html')



def test_update(request):
    """
    Для теста как обновлять созданные таблицы, к таблицы будет добавлятся вася
    Get всегда получает одно значение
    """
    board = Boards.objects.get(pk=19)
    board.title = board.title + ' Вася'
    board.save()
    return HttpResponse(board.title)


def test_update2(request):
    """
    Получаем кортеж где id больше или равно 4
    далее выводим первый в списке элимент
    """
    boards = Boards.objects.filter(id__gte=4)
    return HttpResponse(boards[1].title)



def test_update3(request):
    """
    Получаем кортеж где id больше  4
    используем фор чтоб вывести все список
    """
    boards = Boards.objects.filter(id__gt=4)
    text = ''
    for i in boards:
        text += i.title + '<br>'
    return HttpResponse(text)

def test_delete(request):
    """
    Удалить запись
    """
    board = Boards.objects.get(pk=25)
    board.delete()
    return HttpResponse(f'Успено удаленно {board}')



class BoardsList(generics.ListAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class BoardsListFilter(generics.ListAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        boards = BoardUser.objects.filter(user_id=self.request.user).values_list('board_id_id')
        return Boards.objects.filter(id__in=[boards])


class BoardCreate(generics.CreateAPIView):
    serializer_class = BoardsSerializer



class BoardCreateСonnectionBoard(generics.CreateAPIView):
    serializer_class = BoardsSerializer
    """
    Создание доски  с приаязкой пользователя которые ее создает  пользователя вычленяем из токена
    так как создвать может только авторизированный пользователь
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        перхватываем создание доски и сохраняем ее в переменную (в базу таблица уже ушла)
        """
        board_new = self.create(request, *args, **kwargs)
        """
        создаем приязку пользователя к доске
        """
        BoardUser.objects.create(
            board_id_id=board_new.data['id'],
            user_id=request.user,
            is_user=True,
            is_readonly=False,

        )
        return board_new


# retrieve /update / delete
class BoardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerRUD]



# конкретно ожидает он нас pk то есть мы сами укажим какой  id  использовать прямо в ссылке


class BoardColumnsList(generics.ListAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'board_id',
        'title',
        'sort_index',
    ]


class BoardColumnsFilterList(generics.ListAPIView):
    """
    Пишим фильт  и выводим определенную доску по id
    и смотрим какие колонки существуют
    """

    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer

    def get_queryset(self):
        return BoardColumns.objects.filter(board_id=self.kwargs['boards_id'])


class BoardColumnsCreate(generics.CreateAPIView):
    serializer_class = BoardColumnsSerializer


class BoardColumnsCreateUseBoard(generics.CreateAPIView):
    """
    По токену создаем колонку  при условии что user создатель данной таблицы
    если это не так выводим ощибку 204
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BoardColumnsSerializer

    def post(self, request, *args, **kwargs):
        if (BoardUser.objects.filter(user_id=request.user, board_id_id=request.data['board_id']).count() > 0):
            return self.create(request, *args, **kwargs)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


# retrieve /update / delete
class BoardColumnsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer


class BoardCardsList(generics.ListAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['board_id', 'board_column', ]
    search_fields = ['title', 'description', 'sort_index', 'create_time']
    ordering_fields = ['title', 'create_time', 'sort_index']


class BoardCardsCreate(generics.CreateAPIView):
    serializer_class = BoardCardsSerializer


# сортировка  в Card  по доске board_id
class CardFilter(generics.ListAPIView):
    serializer_class = BoardCardsSerializer

    def get_queryset(self):
        return BoardCards.objects.filter(board_id=self.kwargs['board_id'])


# retrieve /update / delete
class BoardCardsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer


class BoardUserList(generics.ListAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'card_id',
        'board_id',
        'is_user',
        'is_readonly',

    ]


class BoardUserCreate(generics.CreateAPIView):
    serializer_class = BoardUserSerializer


# retrieve /update / delete
class BoardUserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserSerializer


class BoardUserExecutorsList(generics.ListAPIView):
    queryset = BoardUserExecutors.objects.all()
    serializer_class = BoardUserExecutorsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user_id',
        'card_id',

    ]


class BoardUserExecutorsCreate(generics.CreateAPIView):
    serializer_class = BoardUserExecutorsSerializer


# retrieve /update / delete
class BoardUserExecutorsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserExecutorsSerializer


class BoardCardCommentsList(generics.ListAPIView):
    queryset = BoardCardComments.objects.all()
    serializer_class = BoardCardCommentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'user_id',
        'card_id',
        'message',
        'create_time',

    ]


class BoardCardCommentsCreate(generics.CreateAPIView):
    serializer_class = BoardCardCommentsSerializer


# retrieve /update / delete
class BoardCardCommentsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCardComments.objects.all()
    serializer_class = BoardCardCommentsSerializer
