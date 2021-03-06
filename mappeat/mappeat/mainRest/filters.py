import django_filters
from mainRest.models import *

from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ('username',)

class ProductFilter(django_filters.FilterSet):
    """
    Atencion a las mayusculas en el nombre de la family
    """
    family = django_filters.CharFilter(name="product__recomended_family__name")
    restaurant = django_filters.CharFilter(name="restaurant__name")

    class Meta:
        model = Product
        fields = ('name','restaurant', 'family', 'can_be_complement')

class Product_ClassFilter(django_filters.FilterSet):
    """
    Atencion a las mayusculas en el nombre de la family
    """
    family = django_filters.CharFilter(name="recomended_family__name")

    class Meta:
        model = Product_Class
        fields = ('name','family')


class TableFilter(django_filters.FilterSet):
    """
    @note:
    type_table puede ser: M, B, T
    que significan: Mesa, Barra, Terraza respectivamente.
    """
    restaurant = django_filters.CharFilter(name="restaurant__name")

    class Meta:
        model = Table
        fields = ('number', 'restaurant', 'type_table', 'is_available')

class IngredientFilter(django_filters.FilterSet):

    class Meta:
        model = Ingredient
        fields = ('product',)

class Ticket_ResumeFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket_Resume
        fields = ('table', 'is_closed',)

class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket_Resume
        fields = ('table', 'is_closed','date')

class Ticket_DetailFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket_Detail
        fields = ('ticket','sent_kitchen')
