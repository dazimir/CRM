from .models import OrganizationCustomer, IndividualCustomer
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = IndividualCustomer
        fields = ['last_name']


class UserCorpFilter(django_filters.FilterSet):
    class Meta:
        model = OrganizationCustomer
        fields = ['company_name']