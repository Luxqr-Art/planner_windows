from rest_framework import filters


class MyCustomFilter:
    def filter_queryset(self, request, queryset, view):
        return queryset.folter(id__)