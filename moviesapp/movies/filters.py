import django_filters

from .models import Movie

class MovieFilter(django_filters.FilterSet):

    CHOICES = (
        ("year", "Year"),
        ("title", "Title")
    )

    ordering = django_filters.ChoiceFilter(label="Order By", choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Movie
        fields = {
            'title': ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'year' if value == 'year' else 'title'
        print(expression)
        return queryset.order_by(expression)
