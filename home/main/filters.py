from .models import Card
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = ['last_name']