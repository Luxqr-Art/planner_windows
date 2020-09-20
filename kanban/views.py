from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import *
from .models import *


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


class BoardCreate(generics.CreateAPIView):
    serializer_class = BoardsSerializer


# retrieve /update / delete
class BoardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boards.objects.all()
    serializer_class = BoardsSerializer


# конкретно ожидает он нас pk то есть мы сами укажим какой  id  использовать прямо в ссылке


class BoardColumnsList(generics.ListAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer


class BoardColumnsCreate(generics.CreateAPIView):
    serializer_class = BoardColumnsSerializer


# retrieve /update / delete
class BoardColumnsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardColumns.objects.all()
    serializer_class = BoardColumnsSerializer


class BoardCardsList(generics.ListAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer


class BoardCardsCreate(generics.CreateAPIView):
    serializer_class = BoardCardsSerializer


# retrieve /update / delete
class BoardCardsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCards.objects.all()
    serializer_class = BoardCardsSerializer


class BoardUserList(generics.ListAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserSerializer


class BoardUserCreate(generics.CreateAPIView):
    serializer_class = BoardUserSerializer


# retrieve /update / delete
class BoardUserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserSerializer


class BoardUserExecutorsList(generics.ListAPIView):
    queryset = BoardUserExecutors.objects.all()
    serializer_class = BoardUserExecutorsSerializer


class BoardUserExecutorsCreate(generics.CreateAPIView):
    serializer_class = BoardUserExecutorsSerializer


# retrieve /update / delete
class BoardUserExecutorsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserExecutorsSerializer


class BoardCardCommentsList(generics.ListAPIView):
    queryset = BoardCardComments.objects.all()
    serializer_class = BoardCardCommentsSerializer


class BoardCardCommentsCreate(generics.CreateAPIView):
    serializer_class = BoardCardCommentsSerializer


# retrieve /update / delete
class BoardCardCommentsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCardComments.objects.all()
    serializer_class = BoardCardCommentsSerializer
