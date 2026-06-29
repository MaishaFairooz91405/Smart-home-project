import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name='members__user__id')
    is_deleted = django_filters.BooleanFilter()
    users = django_filters.CharFilter(method="filter_users")
    class Meta:
        model = Room
        fields = ['user_id','users', 'is_deleted']

    def filter_users(self,queryset,name,value):
        numbers=value.split(",")
        for user_id in numbers:
            queryset=queryset.filter(members__user__id=user_id)

        return queryset
