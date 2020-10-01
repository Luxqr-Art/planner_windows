from rest_framework import serializers
from .models import *


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = '__all__'




class BoardColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardColumns
        fields = '__all__'


class BoardCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCards
        fields = '__all__'
    # board_id = serializers.SlugRelatedField(slug_field='title', read_only=True)
    # board_column = serializers.SlugRelatedField(slug_field='title', read_only=True)



class BoardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUser
        fields = '__all__'




class BoardUserExecutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUserExecutors
        fields = '__all__'


class BoardCardCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCardComments
        fields = '__all__'
