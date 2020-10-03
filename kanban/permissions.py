from rest_framework import permissions
from .models import BoardUser

class IsOwnerRUD(permissions.BasePermission):
    """
    проверяем
    """
    def has_object_permission(self, request, view, obj):
        """
       в obj.id содержиться доска
       условия выбрать всех юзеров где у нас юзер совпадает с доской если >0 то услоие выполнилось
        """""
        if BoardUser.objects.filter(user_id=request.user, board_id=obj.id).count()>0:
            return True
        return False

