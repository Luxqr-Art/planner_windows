from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import *
from .models import *


def main(request):
    return render(request, 'base.html')


def boards(request):
    return render(request, 'board.html')


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
