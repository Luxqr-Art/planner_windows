from django.shortcuts import render
from rest_framework import generics, filters, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend





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


class BoardsList(generics.ListAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields= ['title']

class BoardCreate(generics.CreateAPIView):
    serializer_class = BoardsSerializer




# retrieve /update / delete
class BoardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer
    permission_classes = [permissions.IsAuthenticated]



# конкретно ожидает он нас pk то есть мы сами укажим какой  id  использовать прямо в ссылке


class BoardColumnsList(generics.ListAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields= [
        'board_id',
        'title',
        'sort_index',
    ]

class BoardColumnsCreate(generics.CreateAPIView):
    serializer_class = BoardColumnsSerializer


# retrieve /update / delete
class BoardColumnsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer


class BoardCardsList(generics.ListAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['board_id', 'board_column',]
    search_fields = ['title', 'description', 'sort_index', 'create_time']
    ordering_fields =['title', 'create_time', 'sort_index']

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
    filterset_fields= [
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
    filterset_fields= [
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
    filterset_fields= [
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
